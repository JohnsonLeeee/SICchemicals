from django.contrib import admin

# Register your models here.

from .models import Chemical, Person, Staff, Student, Location


"""
class ChemicalsMessageInLine(admin.TabularInline):
    model = ChemicalsMessage
    extra = 1


class PersonInLine(admin.TabularInline):
    model = Person
    extra = 1
"""

admin.site.register(Staff)
admin.site.register(Student)
admin.site.register(Location)


@admin.register(Chemical)
class ChemicalAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'chemical_formula', 'CAS', 'size', 'number', 'public_or_private',
                    'location', 'entry_time', 'purchaser', 'approver', 'responsible_man', 'details'
                    ]

    ordering = ('-id',)

    list_editable = ['number']

    list_filter = ['location', 'purchaser',  'approver', 'public_or_private', 'responsible_man']

    # search_fields = ['chemical', 'Person']



