from django.contrib import admin

from staff.models import Employee


class EmployeeAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'title',
    )
    list_filter = ['is_employed']


admin.site.register(Employee, EmployeeAdmin)
