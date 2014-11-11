from django.conf.urls import patterns, url

from projects.views import ProjectDetailView

urlpatterns = patterns(
    '',
    url(
        regex=r'^(?P<slug>[-\w]+)/$',
        view=ProjectDetailView.as_view(),
        name='project_detail'
    ),
)
