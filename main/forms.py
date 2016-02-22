from django import forms
from django.forms.widgets import SelectDateWidget
from datetime import datetime
from .models import Profile

class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('firstName', 'lastName', 'telephone', 'birthdate', 'gender',
        'ocupation', 'pet', 'description', 'lookingIn', 'isSmoker')
        widgets = {
            'birthdate': SelectDateWidget(years = range(datetime.now().year, 1800, -1)),
        }
