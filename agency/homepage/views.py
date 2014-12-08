from django.core.urlresolvers import reverse
from django.contrib.messages.views import SuccessMessageMixin

from contact_form.views import ContactFormView

from headlines.models import Headline
from clients.models import Client
from staff.models import Employee
from projects.models import Project

from .forms import AgencyContactForm


class HomePageView(SuccessMessageMixin, ContactFormView):
    """ The homepage of the agency website. """
    form_class = AgencyContactForm
    success_message = 'Your message was sent successfully'
    template_name = 'home.html'

    def get_success_url(self):
        """ Redirect back to home for success message """
        return reverse('home')

    def get_context_data(self, **kwargs):
        """ Add object context for display. """
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['headline'] = Headline.random_headline.all()
        context['client_list'] = Client.objects.all()
        context['employee_list'] = Employee.public.all()
        context['project_list'] = Project.featured.all()[:10]
        return context
