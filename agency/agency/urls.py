from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from homepage.views import HomePageView

admin.site.site_header = 'The Variable administration'

urlpatterns = patterns(
    '',
    url(
        r'^$',
        HomePageView.as_view(),
        name='home'
    ),
    url(
        r'^contact/',
        include('contact_form.urls')
    ),
    url(
        r'^administration/doc/',
        include('django.contrib.admindocs.urls')
    ),
    url(
        r'^administration/',
        include(admin.site.urls)
    ),
    url(
        r'^pages/',
        include('django.contrib.flatpages.urls')
    ),
    url(
        r'^', include('projects.urls')
    ),
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
                            url(r'^__debug__/', include(debug_toolbar.urls)),
                            )
