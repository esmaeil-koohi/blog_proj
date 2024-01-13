from django import forms

class ContactUsForm(forms.ModelForm):
    text = forms.CharField(max_length=500, label='Your message')