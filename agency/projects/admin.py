from django.contrib import admin
from sorl.thumbnail.admin import AdminImageMixin
from embed_video.admin import AdminVideoMixin
from ordered_model.admin import OrderedModelAdmin

from projects.models import Project, Category, AssetGroup, ImageAsset, \
    TextAsset, VideoAsset


class VideoAssetInline(AdminVideoMixin, admin.StackedInline):
    model = VideoAsset
    extra = 1


class TextAssetInline(admin.StackedInline):
    model = TextAsset
    extra = 1


class ImageAssetInline(AdminImageMixin, admin.StackedInline):
    model = ImageAsset
    extra = 2


class AssetGroupInline(admin.StackedInline):
    model = AssetGroup
    extra = 0


class AssetGroupAdmin(OrderedModelAdmin, admin.ModelAdmin):
    list_display = ('name', 'project', 'move_up_down_links',)
    inlines = [ImageAssetInline, VideoAssetInline, TextAssetInline]


class ProjectAdmin(OrderedModelAdmin, AdminImageMixin, admin.ModelAdmin):
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
