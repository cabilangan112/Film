# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic.detail import DetailView
from django.shortcuts import render
from django.views.generic import View

from .models import Actor
from .models import Films
from .models import Actor

def List_Actor(request):
		movie = Actor.objects.exclude()
		context = {
		'movie' :movie,
		}
		return render(request,"Index.html",context)