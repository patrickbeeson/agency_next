from collections import OrderedDict

from contact_form.forms import ContactForm

from django import forms


class AgencyContactForm(ContactForm):
    """
    Subclass of the ContactForm to add in additional
    fields for the agency website.
    """
    INTEREST_CHOICES = (
        (u'New business', u'New Business'),
        (u'Media inquiry', u'Media inquiry'),
        (u'Employment', u'Employment'),
        (u'Other', u'Other'),
    )
    interest = forms.ChoiceField(
        choices=INTEREST_CHOICES,
        label=u'What are you interested in?',
        required=False,
    )
    phone = forms.RegexField(
        regex=r'^\d{3}[\-]\d{3}[\-]\d{4}([\s][a-z]{3}[\s]\d{1,5})?$',
        help_text='Required format: 555-555-5555 or 555-555-5555 ext 12345',
        required=False,
        label=u'Phone',
        error_message=('Phone number must match the required format!')
    )

    def __init__(self, *args, **kwargs):
        """
        Change the ordering of fields.
        """
        super(AgencyContactForm, self).__init__(*args, **kwargs)
        original_fields = self.fields
        new_ordering = OrderedDict()
        for key in ['name', 'email', 'phone', 'interest', 'body']:
            new_ordering[key] = original_fields[key]
        self.fields = new_ordering
