from django.views.generic import DetailView

from projects.models import Project, AssetGroup


class ProjectDetailView(DetailView):
    """
    View to display individual projects with other projects in context.
    """
    model = Project

    def get_context_data(self, **kwargs):
        """
        Display a list of 10 featured projects.
        """
        context = super(ProjectDetailView, self).get_context_data(**kwargs)
        context['project_list'] = Project.featured.exclude(
            pk=self.object.pk)[:10]
        context['assetgroup_list'] = AssetGroup.objects.filter(
            project_id=self.object.id).select_related('project')
        return context

    def get_queryset(self):
        """
        Allow staff users to see draft projects as if they're live.
        """
        projects = None
        if self.request.user.is_staff:
            projects = Project.objects.all()
        else:
            projects = Project.published.all()
        return projects
