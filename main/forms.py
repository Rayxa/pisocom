from django import forms
from django.forms.widgets import SelectDateWidget
from .models import Profile

class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('firstName', 'lastName', 'telephone', 'birthdate', 'gender',
        'ocupation', 'pet', 'description', 'isSmoker', 'lookingIn')
        widgets = {
            'birthdate': SelectDateWidget(years = range(2016, 1800, -1)),
        }
