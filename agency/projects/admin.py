from django.contrib import admin
from sorl.thumbnail.admin import AdminImageMixin
from embed_video.admin import AdminVideoMixin
from ordered_model.admin import OrderedModelAdmin

from projects.models import Project, Category, AssetGroup, Asset


class AssetGroupInline(OrderedModelAdmin, admin.TabularInline):
    model = AssetGroup
    list_display = ('layout', 'assets', 'move_up_down_links')
    extra = 1


class AssetAdmin(AdminVideoMixin, AdminImageMixin, admin.ModelAdmin):
    inlines = (AssetGroupInline,)


class ProjectAdmin(OrderedModelAdmin, AdminImageMixin, admin.ModelAdmin):
    list_filter = ('categories', 'is_featured', 'status')
    search_fields = ('categories', 'description', 'name')
    list_display = ('name', 'is_featured', 'status', 'move_up_down_links')
    prepopulated_fields = {'slug': ('name',)}
    inlines = (AssetGroupInline,)


class CategoryAdmin(admin.ModelAdmin):
    pass


admin.site.register(Project, ProjectAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Asset, AssetAdmin)
