# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Actor(models.Model):
	first_name = models.CharField(max_length=150)
	last_name = models.CharField(max_length=150)
	middle_name = models.CharField(max_length=150)

	def save(self, *args,**kwargs):
		super(Actor,self).save(*args,**kwargs)
		
	def __str__(self):
		return self.first_name

class Films(models.Model):
	title = models.CharField(max_length=150)
	Year = models.DateTimeField()
	Type = models.ManyToManyField("Genres",related_name="Films")
	Actor = models.ManyToManyField("Actor",related_name="Films")	
		
	def list_films(self):
		return ",".join([title.Films for Films in self.Films.all()])
		
	def save(self, *args,**kwargs):
		super(Films,self).save(*args,**kwargs)
		xxcxxcxcxcxcxcxcxcxcxcx
	def __str__(self):
		return self.title

class Genres(models.Model):
	Type = models.CharField(max_length=150)
	Description = models.CharField(max_length=150)
	
	
	def __str__(self):
		return self.Type	