from django import forms
from django.core.validators import ValidationError

from blog.models import Message


######## for test ########
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


########## method 1 #############
# class MessageForms(forms.Form):
#     title = forms.CharField(max_length=100)
#     text = forms.CharField(widget=forms.Textarea())
#     email = forms.EmailField()


########## method 2 ############
class MessageForms(forms.ModelForm):
    class Meta:
        model = Message
        fields = ('title', 'text', 'email')
