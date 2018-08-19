﻿# -*- coding: utf-8 -*-
from django.forms import ModelForm, CharField, ModelChoiceField, HiddenInput
from django.utils.translation import gettext_lazy as _
from trainer.models import Update, Trainer
from trainer.shortcuts import UPDATE_FIELDS_BADGES, UPDATE_FIELDS_TYPES

class UpdateForm(ModelForm):
	
	class Meta:
		model = Update
		fields = (
			'trainer',
			'xp',
			'meta_source',
			'dex_caught',
			'dex_seen',
			'gym_badges',
			'update_time',
		) + UPDATE_FIELDS_BADGES + UPDATE_FIELDS_TYPES
	
	field_order = (
		'xp',
		'dex_caught',
		'dex_seen',
		'gym_badges',
	) + UPDATE_FIELDS_BADGES + UPDATE_FIELDS_TYPES
	

class RegistrationFormTrainer(ModelForm):
	
	class Meta:
		model = Trainer
		fields = (
			'username',
			'start_date',
			'faction',
			'statistics',
			'daily_goal',
			'total_goal',
			'verification',
		)
	

class RegistrationFormUpdate(UpdateForm):
	
	class Meta:
		model = Update
		fields = (
			'trainer',
			'xp',
			'meta_source',
			'dex_caught',
			'dex_seen',
			'gym_badges',
			'image_proof',
			'update_time',
		) + UPDATE_FIELDS_BADGES + UPDATE_FIELDS_TYPES
	
	field_order = (
		'image_proof',
		'xp',
		'dex_caught',
		'dex_seen',
		'gym_badges',
	) + UPDATE_FIELDS_BADGES + UPDATE_FIELDS_TYPES
