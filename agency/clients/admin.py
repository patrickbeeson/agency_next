from django.contrib import admin

from sorl.thumbnail.admin import AdminImageMixin

from clients.models import Client


class ClientAdmin(AdminImageMixin, admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Client, ClientAdmin)
