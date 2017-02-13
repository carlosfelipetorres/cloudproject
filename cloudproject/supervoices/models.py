from __future__ import unicode_literals

from django.db import models

class User(models.Model):
	ADMIN = 'ADMIN'
	SPEAKER = 'SPEAKER'
	ROLES = (
		(ADMIN, 'Admin'),
		(SPEAKER, 'Speaker'),
	)
	role = models.CharField(
		max_length=10,
		choices=ROLES,
		default=ADMIN,
	)
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	email = models.CharField(max_length=200)
	password = models.CharField(max_length=200)
	date_created = models.DateTimeField('date created')


class Contest(models.Model):
	name = models.CharField(max_length=200)
	banner = models.CharField(max_length=500)
	url = models.CharField(max_length=500)
	guion = models.CharField(max_length=1000)
	recommendations = models.CharField(max_length=1000)
	valor = models.IntegerField(default=20)
	date_begin = models.DateTimeField('date begin')
	date_finish = models.DateTimeField('date finish')


class Audio(models.Model):
	email = models.CharField(max_length=200)
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	date_uploaded = models.DateTimeField('date uploaded')
	original_audio = models.CharField(max_length=500)
	converted_audio = models.CharField(max_length=500)
	PROCESS = 'PROCESS'
	CONVERTED = 'CONVERTED'
	STATES = (
		(PROCESS, 'Process'),
		(CONVERTED, 'Converted'),
	)
	state = models.CharField(
		max_length=10,
		choices=STATES,
		default=PROCESS,
	)


class File_contest_user(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	contest = models.ForeignKey(Contest, on_delete=models.CASCADE)
	audio = models.ForeignKey(Audio, on_delete=models.CASCADE)
	

