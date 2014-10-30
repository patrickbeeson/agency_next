from django.contrib import admin
from sorl.thumbnail.admin import AdminImageMixin

from projects.models import Project, Category


class ProjectAdmin(AdminImageMixin, admin.ModelAdmin):
    list_filter = ('categories', 'is_featured', 'status')
    search_fields = ('categories', 'description', 'name')
    list_display = ('name', 'is_featured', 'status')
    prepopulated_fields = {'slug': ('name',)}


class CategoryAdmin(admin.ModelAdmin):
    pass


admin.site.register(Project, ProjectAdmin)
admin.site.register(Category, CategoryAdmin)
