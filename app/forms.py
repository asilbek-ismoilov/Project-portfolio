from django import forms
from django.forms import ModelForm
from .models import Contact

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ["name", "email", "message"]

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        message = cleaned_data.get('message')

        # Name validation
        if name:
            if len(name) < 3:
                self.add_error('name', "Minimum 3 characters required")
        else:
            self.add_error('name', "Name is required")

        # Message validation
        if not message:
            self.add_error('message', "Message is required")

        return cleaned_data

    def clean_email(self):
        email = self.cleaned_data.get('email')

        # Email validation: Check if the email domain is correct (example.com)
        if email:
            if '@example.com' not in email:
                raise forms.ValidationError("Email must be from the domain '@example.com'.")
        
        return email
