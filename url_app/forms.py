from django import forms

from .models import UserData

class UserDataForm(forms.ModelForm):
    class Meta:
        model = UserData
        fields = ('text', 'secret_key')

class SecretKeyForm(forms.Form):
    secret_key = forms.CharField(max_length=10)

