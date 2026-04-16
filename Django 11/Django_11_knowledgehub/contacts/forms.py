from django import  forms
from django.core.exceptions import ValidationError
from django.template.defaultfilters import first


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
