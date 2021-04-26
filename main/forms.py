from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from .models import *
from django.contrib.auth import password_validation
from django.core.exceptions import ValidationError
# from .models import user_registrated


class CusForm(forms.ModelForm):
    email = forms.EmailField(label='Почтовый ящик', max_length=50)
    name = forms.CharField(label='Ваше имя', max_length=25)
    phone = forms.CharField(label='Ваш номер телефона', max_length=12)
    rassilka = models.BooleanField(default=True, verbose_name='Согласны ли вы получать рассылку?')

    class Meta:
        model = Customers
        fields = ['email', 'name', 'phone', 'rassilka']


class UserForm(forms.Form):
    login = forms.CharField(label='Имя пользователя', max_length=50)
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)


class RegisterUserForm(forms.ModelForm):
    username = forms.CharField(required=True, label='Имя пользователя')
    email = forms.EmailField(required=True, label='Адрес электронной почты')
    password1 = forms.CharField(required=True, widget=forms.PasswordInput, label='Введите пароль')
    password2 = forms.CharField(widget=forms.PasswordInput, required=True, label='Повторите ваш пароль')
    first_name = forms.CharField(required=True, label='Ваше имя')
    last_name = forms.CharField(required=True, label='Ваша фамилия')
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name']

    def clean_password(self):
        password1=self.cleaned_data['password1']
        if password1:
            password_validation.validate_password(password1)
        return password1


    def clean(self):
        super().clean()
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        if password1 and password2 and password1 != password2:
            errors = {'password2':ValidationError('Введеные пароли не совпадают', code='password_mismatch')}
            raise ValidationError(errors)


    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        user.is_active = True
        user.is_activated = True
        if commit:
            user.save()
        return user


class ChangePasswordForm(forms.Form):
    old_password = forms.CharField(widget=forms.PasswordInput, max_length=75, label='Введите текущий пароль')
    new_password1 = forms.CharField(widget=forms.PasswordInput, max_length=75, label='Введите новый пароль')
    new_password2 = forms.CharField(widget=forms.PasswordInput, max_length=75, label='Введите повторно новый пароль')
class Meta:
    model = CustomUser
    fields = ['old_password', 'new_password1', 'new_password2']