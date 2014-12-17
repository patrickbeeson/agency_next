from django.contrib import admin
from sorl.thumbnail.admin import AdminImageMixin
from embed_video.admin import AdminVideoMixin
from ordered_model.admin import OrderedModelAdmin
from nested_inline.admin import NestedStackedInline, NestedModelAdmin

from projects.models import Project, Category, AssetGroup, ImageAsset, \
    TextAsset, VideoAsset


class CommonAssetAdmin(admin.ModelAdmin):
    list_display = ('name', 'group', 'project')
    readonly_fields = ('project',)

    def project(self, obj):
        project = Project.objects.filter(
            assetgroup__project_id=obj.group.project.id).values_list(
            'name', flat=True)[0]
        return project
    project.short_description = 'Project'


class ImageAssetAdmin(CommonAssetAdmin):
    pass


class TextAssetAdmin(CommonAssetAdmin):
    pass


class VideoAssetAdmin(CommonAssetAdmin):
    pass


class ImageAssetInline(AdminImageMixin, NestedStackedInline):
    model = ImageAsset
    extra = 2


class TextAssetInline(NestedStackedInline):
    model = TextAsset
    extra = 1


class VideoAssetInline(AdminVideoMixin, NestedStackedInline):
    model = VideoAsset
    extra = 1


class AssetGroupInline(NestedStackedInline):
    model = AssetGroup
    extra = 5
    inlines = [ImageAssetInline, TextAssetInline, VideoAssetInline]


class AssetGroupAdmin(OrderedModelAdmin, admin.ModelAdmin):
    list_display = (
        'name',
        'asset_group_type',
        'project',
        'order',
        'move_up_down_links'
    )
    list_filter = ('project', 'asset_group_type')
    inlines = [ImageAssetInline, TextAssetInline, VideoAssetInline]


class ProjectAdmin(OrderedModelAdmin, AdminImageMixin, NestedModelAdmin):
    list_filter = ('categories', 'is_featured', 'status')
    search_fields = ('categories', 'description', 'name')
    list_display = ('name', 'is_featured', 'status', 'move_up_down_links')
    prepopulated_fields = {'slug': ('name',)}
    inlines = [AssetGroupInline]


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Project, ProjectAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(AssetGroup, AssetGroupAdmin)
admin.site.register(ImageAsset, ImageAssetAdmin)
admin.site.register(VideoAsset, VideoAssetAdmin)
admin.site.register(TextAsset, TextAssetAdmin)
