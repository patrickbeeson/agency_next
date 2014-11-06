from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = 'The Variable administration'

urlpatterns = patterns('',
    url(r'^$', 'homepage.views.HomePageView', name='home'),
    url(r'^administration/doc/', include('django.contrib.admindocs.urls')),
    url(r'^administration/', include(admin.site.urls)),
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
                            url(r'^__debug__/', include(debug_toolbar.urls)),
                            )
