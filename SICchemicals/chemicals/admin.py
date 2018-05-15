from django.contrib import admin

# Register your models here.

from .models import Chemical, Person, Staff, Student, Location, ChemicalsMessage

admin.site.register(Chemical, Person, Staff, Student, Location, ChemicalsMessage)
