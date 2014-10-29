from django.contrib import admin

from headlines.models import Headline


class HeadlineAdmin(admin.ModelAdmin):
    list_display = ('headline',)

admin.site.register(Headline, HeadlineAdmin)
