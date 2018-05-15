from django.contrib import admin

# Register your models here.

from .models import Chemical, Person, Staff, Student, Location, ChemicalsMessage

admin.site.register(Staff)
admin.site.register(Student)
admin.site.register(Location)
admin.site.register(ChemicalsMessage)


@admin.register(Chemical)
class ChemicalAdmin(admin.ModelAdmin):
    list_display = ['id', 'chemical', 'public_or_private', 'size', 'number',
                    'location', 'entry_time', 'purchaser', 'approver', 'responsible_man'
                    ]

    ordering = ('id',)

    list_editable = ['number']

    list_filter = ['location', 'purchaser',  'approver', 'responsible_man']

    search_fields = ['chemical', 'Person']



