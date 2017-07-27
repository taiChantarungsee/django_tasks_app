from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):

	number = models.IntegerField(null=True) #change into a uid? Also need to set this auto.
	title = models.CharField(max_length=20)
	text = models.TextField(blank=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	completed = models.NullBooleanField(null=True)
	date_created = models.DateField(blank=True, null=True)
	date_completed = models.DateField(blank=True, null=True)

	def __str__(self):
		return self.title

#put lots of stuff in models and forms to show how I would deal with it.