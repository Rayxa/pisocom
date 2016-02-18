from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from captcha.fields import CaptchaField

class RegistrationForm(UserCreationForm):

    email = forms.EmailField(
        required = True
    )

    captcha = CaptchaField(
        label = 'Captcha'
    )
    
    tos = forms.BooleanField(
        widget = forms.CheckboxInput,
        label = 'He leído y acepto las condiciones de uso',
        error_messages={'required': 'Debes aceptar las condiciones de uso para continuar'}
    )
    
    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
        
        
