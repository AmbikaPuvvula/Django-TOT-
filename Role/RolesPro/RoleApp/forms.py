from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import ModelForm
from . models import Update


class UserReg(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={"class": "form-control border-success", "placeholder": "Enter password"}))
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={"class": "form-control border-success", "placeholder": "Enter Confirm password", }))

    class Meta:
        model = User
        fields = ['username', 'email']
        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control border-success", "placeholder": "Enter username", "requires": True, }),
            "email": forms.TextInput(attrs={"class": "form-control border-success", "placeholder": "Enter email", "requires": True, })
        }


class UpdateProfile(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter username", "requires": True, }),
            "first_name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Update firstname", "requires": True, }),
            "last_name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Update lastname", "requires": True, }),
            "email": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter email", "requires": True, }),
        }


class UpdateUserProfile(ModelForm):
    class Meta:
        model = Update
        # fields = '__all__'
        fields = ['age', 'gender', 'image']
        widgets = {
            "age": forms.NumberInput(attrs={
                "class": "form-control",
            }),
            "gender": forms.Select(attrs={
                "class": "form-control",
            }),
        }
