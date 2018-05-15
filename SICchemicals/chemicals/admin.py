from django.contrib import admin

# Register your models here.

from .models import Chemical, Person, Staff, Student, Location, ChemicalsMessage

admin.site.register(Staff)
admin.site.register(Student)
admin.site.register(Location)
admin.site.register(ChemicalsMessage)


@admin.register(Chemical)
class ChemicalAdmin(admin.ModelAdmin):
    list_display = ['id', 'CAS', 'public_or_private', 'size', 'number',
                    'location', 'entry_time', 'purchaser', 'approver', 'responsible_man'
                    ]

    list_per_page = 30

    ordering = ('id',)

    list_editable = ['CAS', 'public_or_private', 'size',
                     'number', 'location', 'purchaser', 'approver', 'responsible_man'
                     ]



