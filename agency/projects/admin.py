from django.contrib import admin
from sorl.thumbnail.admin import AdminImageMixin
from embed_video.admin import AdminVideoMixin
from ordered_model.admin import OrderedModelAdmin
from nested_inline.admin import NestedStackedInline, NestedModelAdmin

from projects.models import Project, Category, AssetGroup, Asset


class AssetInline(AdminVideoMixin, AdminImageMixin, NestedStackedInline):
    model = Asset
    extra = 2


class AssetGroupInline(NestedStackedInline):
    model = AssetGroup
    extra = 5
    inlines = [AssetInline]


class AssetAdmin(admin.ModelAdmin):
    list_display = ('name', 'asset_type', 'group', 'project')
    readonly_fields = ('project',)
    list_filter = ('asset_type',)

    def project(self, obj):
        project = Project.objects.filter(
            assetgroup__project_id=obj.group.project.id).values_list(
            'name', flat=True)[0]
        return project
    project.short_description = 'Project'


class AssetGroupAdmin(OrderedModelAdmin, admin.ModelAdmin):
    list_display = ('name', 'asset_group_type', 'project', 'order', 'move_up_down_links')
    list_filter = ('project', 'asset_group_type')
    inlines = [AssetInline]


class ProjectAdmin(OrderedModelAdmin, AdminImageMixin, NestedModelAdmin):
    list_filter = ('categories', 'is_featured', 'status')
    search_fields = ('categories', 'description', 'name')
    list_display = ('name', 'is_featured', 'status', 'move_up_down_links')
    prepopulated_fields = {'slug': ('name',)}
    inlines = [AssetGroupInline]


class CategoryAdmin(admin.ModelAdmin):
    pass


admin.site.register(Project, ProjectAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(AssetGroup, AssetGroupAdmin)
admin.site.register(Asset, AssetAdmin)
