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
        required=True,
        widget=forms.Select(
            attrs={
                'class': 'form-select',
                'data-parsley-trigger': 'change',
                'data-parsley-error-message': 'Knowing your subject is very important to us.',
            }
        )
    )
    phone = forms.RegexField(
        regex=r'^\d{3}[\-]\d{3}[\-]\d{4}([\s][a-z]{3}[\s]\d{1,5})?$',
        help_text='Required format: 555-555-5555 or 555-555-5555 ext 12345',
        required=False,
        label=u'Phone',
        error_message=('Phone number must match the required format!'),
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Phone (format: 555-555-5555 or 555-555-5555 ext 12345)',
                'class': 'form-control',
                'data-parsley-trigger': 'change',
                'data-parsley-error-message': 'Oops! Is this a valid phone number?',
            }
        )
    )

    def __init__(self, *args, **kwargs):
        """
        Change the ordering of fields.
        """
        super(AgencyContactForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget = forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Name *',
                'data-parsley-trigger': 'change',
                'data-parsley-error-message': 'We need your name',
                'required': 'required',
            }
        )
        self.fields['name'].required = True
        self.fields['email'].widget = forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Email *',
                'data-parsley-trigger': 'change',
                'data-parsley-error-message': 'We need a valid email address',
                'required': 'required',
            }
        )
        self.fields['email'].required = True
        self.fields['body'].widget = forms.Textarea(
            attrs={
                'class': 'form-textarea',
                'placeholder': 'Your message *',
                'data-parsley-trigger': 'change',
                'data-parsley-error-message': 'Looks like you forgot to include your message.',
                'required': 'required',
            }
        )
        self.fields['body'].required = True
        original_fields = self.fields
        new_ordering = OrderedDict()
        for key in ['name', 'email', 'phone', 'interest', 'body']:
            new_ordering[key] = original_fields[key]
        self.fields = new_ordering
