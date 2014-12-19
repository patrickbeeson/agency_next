from django.contrib import admin
from ordered_model.admin import OrderedModelAdmin

from staff.models import Employee


class EmployeeAdmin(OrderedModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'title',
        'order',
        'move_up_down_links',
    )
    list_filter = ['is_employed']


admin.site.register(Employee, EmployeeAdmin)
