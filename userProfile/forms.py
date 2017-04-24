from django import forms
from .models import *

class userProfileForm(forms.ModelForm):

    class Meta:
        model = BaseCustomUser
        fields = ['email', 'first_name', 'middle_name', 'last_name',
                  'gender', 'phone_number', 'birthday', 'address']
