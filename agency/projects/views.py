from django.views.generic import DetailView

from projects.models import Project


class ProjectDetailView(DetailView):
    model = Project

    def get_context_data(self, **kwargs):
        """
        Display a list of 10 featured projects.
        """
        context = super(ProjectDetailView, self).get_context_data(**kwargs)
        context['project_list'] = Project.featured.all()[:10]
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
