# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic.detail import DetailView
from django.shortcuts import render
from django.views.generic import View

from .models import Actor
from .models import Films
from .models import Genres

def List_Actor(request):
		movie = Actor.objects.exclude()
		context = {
		'movie' :movie,
		}
		return render(request,"Index.html",context)
		
class FilmsDetailView(DetailView):
		model = Films

		template_name ="filmss.html"

def get_context_data(self, **kwargs):
		context = super(FilmsDetailView, self).get_context_data(**kwargs)
		movie = Actor.objects.exclude()
		context = {
		'movie' :movie,
		}
		return context
		
class Film_list(View):
	def get(self,request):
		film = Films.objects.all()
		movie = Actor.objects.exclude()
		context = {
		'film' :film,
		'movie' :movie,
		}
		return render(request,"film.html",context)
		
class Genrelist(View):
	def get(self,request):
		genres = Genres.objects.all()
		context = {
		'genres' :genres,
		}
		return render(request,"Genre.html",context)