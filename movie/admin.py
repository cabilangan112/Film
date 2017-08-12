# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Actor
from .models import Films
from .models import Genres


class movieAdmin(admin.ModelAdmin):
	fieldset = [("movie Actor", {"field":["first_name","last_name"]})
	]
	
def list_films(self, obj):
	return obj.list_Films()
	
class FilmsAdmin(admin.ModelAdmin):
	list_display = ("title","Year",)
	list_editable = ("Year",)
	list_filter = ("title",)
	search_fields = ("title","Year",)
	
class ActorAdmin(admin.ModelAdmin):
	list_display = ("first_name","last_name",)
	list_editable = ("last_name",)
	list_filter = ("middle_name",)
	search_fields = ("first_name","last_name",)

class GenresAdmin(admin.ModelAdmin):
	list_display = ("Type","Description",)
	list_editable = ("Description",)
	list_filter = ("Description",)
	search_fields = ("Type","Description",)
	
	
admin.site.register(Actor,ActorAdmin)
admin.site.register(Films,FilmsAdmin)
admin.site.register(Genres,GenresAdmin)
