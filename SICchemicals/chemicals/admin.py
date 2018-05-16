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
admin.site.site_header = u"上硅所碳化物组药品管理系统"
admin.site.site_title = u"硅所碳化物组药品管理"
admin.site.register(Staff)
admin.site.register(Student)
admin.site.register(Location)


@admin.register(Chemical)
class ChemicalAdmin(admin.ModelAdmin):

    """
    fieldsets = [
        (u"基本信息", {'fields': [('name', 'chemical_formula', 'CAS', 'size', 'number', 'public_or_private',
                               'location', 'purchaser', 'approver', 'responsible_man')]}),
        (u"备注", {'fields': ['details']})
    ]
    """

    list_display = ['id', 'name', 'chemical_formula', 'CAS', 'size', 'number', 'public_or_private',
                    'location', 'entry_time', 'purchaser', 'approver', 'responsible_man', 'details'
                    ]

    ordering = ('-id',)

    list_editable = ['number']

    list_filter = ['location', 'purchaser',  'approver', 'public_or_private', 'responsible_man']

    search_fields = ['name', 'chemical_formula', 'CAS', 'location__location',
                     'purchaser__name', 'approver__name', 'responsible_man__name', 'details']

    list_display_links = ['id', 'name', 'chemical_formula']



