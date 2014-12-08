from django.views.generic import TemplateView
from django.views.generic.edit import FormView

from contact_form.views import ContactFormView

from headlines.models import Headline
from clients.models import Client
from staff.models import Employee
from projects.models import Project

from .forms import AgencyContactForm


class AgencyContactFormView(ContactFormView, FormView):
    """
    Inherit ContactFormView but with new form reference
    """
    form_class = AgencyContactForm
    success_message = 'Your message was sent successfully'


class HomePageView(TemplateView):
    """ The homepage of the agency website. """
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        """ Add object context for display. """
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['headline'] = Headline.random_headline.all()
        context['client_list'] = Client.objects.all()
        context['employee_list'] = Employee.public.all()
        context['project_list'] = Project.featured.all()[:10]
        return context
