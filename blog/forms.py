from django import forms
from django.core.validators import ValidationError


class ContactUsForm(forms.Form):
    name = forms.CharField(max_length=10, label='Your message', required=False)
    text = forms.CharField(max_length=10, label='Your message')

    def clean(self):
        name = self.cleaned_data.get('name')
        text = self.cleaned_data.get('text')
        if name == text:
            raise ValidationError('name and text are same', code='name_text_same')

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if 'a' in name:
            raise ValidationError('a can not be in name')
        return name


