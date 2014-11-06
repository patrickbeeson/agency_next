from django.contrib import admin
from sorl.thumbnail.admin import AdminImageMixin
from embed_video.admin import AdminVideoMixin
from ordered_model.admin import OrderedModelAdmin

from projects.models import Project, Category, AssetGroup, Asset


# class AssetGroupInline(AdminVideoMixin, AdminImageMixin, admin.StackedInline):
#     model = AssetGroup
#     extra = 1


class AssetInline(AdminVideoMixin, AdminImageMixin, admin.StackedInline):
    model = Asset
    extra = 1

class AssetAdmin(admin.ModelAdmin):
    pass


class AssetGroupAdmin(OrderedModelAdmin, admin.ModelAdmin):
    list_display = ('layout', 'move_up_down_links',)
    # inlines = [AssetInline]


class ProjectAdmin(OrderedModelAdmin, AdminImageMixin, admin.ModelAdmin):
    list_filter = ('categories', 'is_featured', 'status')
    search_fields = ('categories', 'description', 'name')
    list_display = ('name', 'is_featured', 'status', 'move_up_down_links')
    prepopulated_fields = {'slug': ('name',)}
    inlines = [AssetInline]


class CategoryAdmin(admin.ModelAdmin):
    pass


admin.site.register(Project, ProjectAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(AssetGroup, AssetGroupAdmin)
admin.site.register(Asset, AssetAdmin)
