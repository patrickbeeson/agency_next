from django.contrib import admin
from sorl.thumbnail.admin import AdminImageMixin
from embed_video.admin import AdminVideoMixin
from ordered_model.admin import OrderedModelAdmin

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
    fieldsets = (
        (None, {
            'fields': ('image', 'caption',)
        }),
        ('Admin options', {
            'classes': ('collapse',),
            'fields': ('name', 'description', 'group', 'project',)
        }),
    )


class TextAssetAdmin(CommonAssetAdmin):
    fieldsets = (
        (None, {
            'fields': ('title', 'text',)
        }),
        ('Admin options', {
            'classes': ('collapse',),
            'fields': ('name', 'description', 'group', 'project',)
        }),
    )


class VideoAssetAdmin(CommonAssetAdmin):
    fieldsets = (
        (None, {
            'fields': ('video', 'caption',)
        }),
        ('Admin options', {
            'classes': ('collapse',),
            'fields': ('name', 'description', 'group', 'project',)
        }),
    )


class ImageAssetInline(AdminImageMixin, admin.StackedInline):
    model = ImageAsset
    extra = 2


class TextAssetInline(admin.StackedInline):
    model = TextAsset
    extra = 1


class VideoAssetInline(AdminVideoMixin, admin.StackedInline):
    model = VideoAsset
    extra = 1


class AssetGroupAdmin(OrderedModelAdmin, admin.ModelAdmin):
    list_display = (
        'name',
        'asset_group_type',
        'project',
        'move_up_down_links'
    )
    list_filter = ('project', 'asset_group_type')
    inlines = [ImageAssetInline, TextAssetInline, VideoAssetInline]


class ProjectAdmin(OrderedModelAdmin, AdminImageMixin):
    list_filter = ('categories', 'is_featured', 'status')
    search_fields = ('categories', 'description', 'name')
    list_display = ('name', 'is_featured', 'status', 'move_up_down_links')
    prepopulated_fields = {'slug': ('name',)}


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Project, ProjectAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(AssetGroup, AssetGroupAdmin)
admin.site.register(ImageAsset, ImageAssetAdmin)
admin.site.register(VideoAsset, VideoAssetAdmin)
admin.site.register(TextAsset, TextAssetAdmin)
