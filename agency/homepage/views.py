from django.views.generic import TemplateView

from headlines.models import Headline
from clients.models import Client
from staff.models import Employee
from projects.models import Project


class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['headline_list'] = Headline.objects.all()
        context['client_list'] = Client.objects.all()
        context['employee_list'] = Employee.public.all()
        context['project_list'] = Project.featured.all()
        return context
