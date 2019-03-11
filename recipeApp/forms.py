from django import forms
from .models import RecipieInfo,NewUser

class NewUserForm(forms.ModelForm):
    class Meta:
        model=NewUser
        exclude=['userTableForeignKey']


class RecipieInfoForm(forms.ModelForm):
    class Meta:
        model=RecipieInfo
        exclude=['keytoNewUser']

class changeProfile(forms.ModelForm):
    class Meta:
        model=NewUser
        fields=['name','email','picture']