from django import forms
from django.forms import ModelForm
from FormsApp.models import Register

genders = [('Male', "Male"), ('Female', "Female")]
branchs = [('None', 'None'), ('ECE', "ECE"),
           ('MEC', "MEC"), ('CSE', "CSE"), ('IT', "IT")]
lang = [('Telugu', "Telugu"), ('English', "English"),
        ('Hindi', "Hindi"), ('Malayalam', "Malayalam")]


class DynamicFormCreation(forms.Form):
    firstname = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': "Enter Firstname", 'class': 'form-control'}))
    lastname = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': "Enter Lastname", 'class': 'form-control'}))
    age = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': "Enter Age", 'class': 'form-control'}))
    email = forms.CharField(widget=forms.EmailInput(
        attrs={'placeholder': "Enter email", 'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': "Enter Password", 'class': 'form-control'}))
    url = forms.CharField(widget=forms.URLInput(
        attrs={'placeholder': "Enter URL", 'class': 'form-control'}))
    gender = forms.ChoiceField(widget=forms.RadioSelect(
        attrs={'class': 'form-group radio-inline'}), choices=genders)
    branch = forms.ChoiceField(widget=forms.Select(
        attrs={'class': 'form-control'}), choices=branchs)
    languages = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'checkbox-inline mb-2 form-group'}), choices=lang)


# class RegisterForm(ModelForm):
#     class Meta:
#         model = Register
#         # For specific fields generate them in a list['name','age'] like this
#         # fields = ['name','age']
#         fields = '__all__'
#         widgets = {
#             "name": forms.TextInput(attrs={"placeholder": "Enter name"}),
#             "mobile_no": forms.TextInput(attrs={"placeholder": "Enter Mobile number"}),
#             "age": forms.NumberInput(attrs={"required": False, "placeholder": "Enter Age"}),
#             "gender": forms.RadioSelect(),
#             "branch": forms.Select(),
#             # "lang": forms.CheckboxSelectMultiple(),
#         }


class Reg(forms.ModelForm):
    class Meta:
        model = Register
        fields = ['name', 'mobile_no', 'age', 'gender', 'branch']
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter name"}),
            "mobile_no": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter Mobile number"}),
            "age": forms.NumberInput(attrs={"class": "form-control", "required": False, "placeholder": "Enter Age"}),
            "gender": forms.RadioSelect(attrs={"type": "radio",
                                               "placeholder": "select Gender",
                                               }),
            "branch": forms.Select(attrs={"class": "form-control"}),
        }
