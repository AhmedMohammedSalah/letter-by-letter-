from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from django import forms
from django.contrib.auth.forms import AuthenticationForm


class SignupForm(forms.Form):   
    nid = forms.CharField(
        label='الرقم القومي',
        max_length=14,
        min_length=14,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control mt-2' , 'minlength': '14', 'maxlength': '14', 'pattern': '[0-9]{14}', 'required': 'true'})
    )
    fname = forms.CharField(
        label='الاسم',
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control mt-2', 'required': 'true'})
    )
    image = forms.ImageField(
        label='الصورة',
        required=False,
        widget=forms.FileInput(attrs={'class': 'form-control-file mt-2', 'accept': 'image/*'})
    )
    age = forms.IntegerField(
        label='العمر',
        min_value=18,
        required=True,
        widget=forms.NumberInput(attrs={'class': 'form-control mt-2', 'min': '18', 'required': 'true'})
    )