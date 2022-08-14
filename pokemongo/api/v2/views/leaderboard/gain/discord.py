from __future__ import annotations

from django.db.models import Q, QuerySet, Subquery
from oauth2_provider.contrib.rest_framework.authentication import OAuth2Authentication
from requests import Response
from rest_framework.authentication import SessionAuthentication
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request

from core.models.discord import DiscordGuild, DiscordRole
from pokemongo.api.v2.views.leaderboard.gain.interface import iGainLeaderboardView
from pokemongo.api.v2.views.leaderboard.interface import TrainerSubset
from pokemongo.models import Trainer


class DiscordGainLeaderboardView(iGainLeaderboardView):
    SUBSET = TrainerSubset.DISCORD

    authentication_classes = [OAuth2Authentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def get_leaderboard_title(self) -> str:
        return str(self.guild)

    @staticmethod
    def get_guild(id: int | str) -> DiscordGuild:
        return DiscordGuild.objects.get(id=id)

    def parse_args(self, request: Request) -> None:
        super().parse_args(request)
        self.guild: DiscordGuild = self.get_guild(request.query_params.get("guild_id"))

    def get_trainer_queryset(self) -> QuerySet[Trainer]:
        queryset = super().get_trainer_queryset()

        opt_out_roles: QuerySet[DiscordRole] = self.guild.roles.filter(
            data__name__in=["NoLB", "TrainerDex Excluded"]
        ).union(
            self.guild.roles.filter(exclude_roles_community_membership_discord__discord=self.guild)
        )

        queryset = queryset.filter(owner__socialaccount__guilds__id=self.guild.id).exclude(
            owner__socialaccount__guild_memberships__data__roles__contains=Subquery(
                opt_out_roles.values_list("id", flat=True)
            )
        )

        return queryset

    def in_guild(self, request: Request) -> bool:
        if not request.user or not request.user.is_authenticated:
            return False

        if request.user.is_superuser:
            return True

        return request.user.socialaccount_set.filter(
            Q(guild_memberships__guild=self.guild) & Q(guild_memberships__active=True)
        ).exists()

    def get(self, request: Request) -> Response:
        if not self.in_guild(request):
            raise PermissionDenied("You are not in this guild", status=403)

        return super().get(request)
