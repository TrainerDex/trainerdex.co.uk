from decimal import Decimal
from typing import NamedTuple

from django.db import models
from django.utils.translation import gettext_lazy as _


class MedalData(NamedTuple):
    stat_id: int
    bronze: int | Decimal | None
    silver: int | Decimal | None
    gold: int | Decimal | None
    platinum: int | Decimal | None
    reversable: bool
    sortable: bool
    name: str
    verbose_name: str
    tooltip: str


class BaseStatistic(models.Field):
    def __init__(
        self,
        /,
        stat_id: int = None,
        bronze: int | Decimal | None = None,
        silver: int | Decimal | None = None,
        gold: int | Decimal | None = None,
        platinum: int | Decimal | None = None,
        reversable: bool = False,
        sortable: bool = True,
        **kwargs,
    ):
        self.stat_id = stat_id
        if bronze is not None:
            assert bronze < silver < gold < (platinum or float("inf"))
        self.bronze, self.silver, self.gold, self.platinum = bronze, silver, gold, platinum
        self.reversable, self.sortable = reversable, sortable

        super().__init__(**kwargs)

    @property
    def medal_data(self) -> MedalData:
        return MedalData(
            stat_id=self.stat_id,
            bronze=self.bronze,
            silver=self.silver,
            gold=self.gold,
            platinum=self.platinum,
            reversable=self.reversable,
            sortable=self.sortable,
            name=self.name,
            verbose_name=self.verbose_name,
            tooltip=self.help_text,
        )


class IntegerStatistic(BaseStatistic, models.PositiveBigIntegerField):
    description = _("Integer Statistic")


class BigIntegerStatistic(BaseStatistic, models.BigIntegerField):
    description = _("Integer Statistic")


class DecimalStatistic(BaseStatistic, models.DecimalField):
    description = _("Decimal Statistic")
