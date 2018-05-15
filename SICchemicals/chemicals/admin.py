from django.contrib import admin

# Register your models here.

from .models import Chemical, Person, Staff, Student, Location, ChemicalsMessage

admin.site.register(Chemical)
admin.site.register(Staff)
admin.site.register(Student)
admin.site.register(Location)
admin.site.register(ChemicalsMessage)





