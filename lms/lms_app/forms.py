from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms
from .models import Loginadmin, SignUpAdmin, addBooks
from .models import SignUpUser


class BookForm(forms.ModelForm):
    class Meta:
        model= addBooks
        fields=[
            'category',
            'title',
            'author',
            'price',
            'publication_year',
            'ISBN',
        ]        

class SignUpForm(forms.ModelForm):
    class Meta:
        model= SignUpUser
        fields=[
            'firstName',
            'lastName',
            'email',
            'password',
            'confirm_password',
        ]
class AdminSignUpForm (forms.ModelForm):
    class Meta:
        model = SignUpAdmin
        fields = '__all__'       

class LoginAdminForm(forms.ModelForm):
    class Meta:
        model = Loginadmin
        fields = '__all__'

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name', 
            'username',
            'email',
            'password1',
            'password2'
        ]

class EditProfileForm (UserChangeForm):
    class Mete:
        model = User
        fields = [             
            'email',
            'first_name',
            'last_name'   
        ]