from __future__ import unicode_literals

from django.db import models

class User(models.Model):

	name = models.CharField(max_length=20)
	password = models.CharField(max_length=20)

	def save(self):
		self.save()

	def __str__(self):
		return self.title

class Task(models.Model):

	title = models.CharField(max_length=20)
	text = models.TextField(blank=True)
	user = models.CharField(max_length=20, blank=True)
	status = models.BooleanField(blank=True)
	date_created = models.DateField(blank=True, null=True)
	date_completed = models.DateField(blank=True, null=True)

	def save(self):
		self.save()

	def __str__(self):
		return self.title