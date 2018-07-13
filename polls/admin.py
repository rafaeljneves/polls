__author__ = 'rafaelj'

from django.contrib import admin
from django.contrib.auth.models import User
from polls.models import Poll, Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class PollAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,              {'fields': ['questao']}),
        ('Data Publicacao', {'fields': ['data_publicacao'], 'classes': ['collapse']})
    ]
    inlines = [ChoiceInline]

admin.site.register(Poll, PollAdmin)



