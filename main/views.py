from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views.generic import CreateView
from django.contrib.auth import login
from django.contrib.auth.views import LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CusForm, DataModelUser
from django.contrib.auth import authenticate, login
from .forms import *
from django.views.generic.base import TemplateView
from django.urls import reverse, reverse_lazy
from django.core.signing import BadSignature
# from .utilities import signer
# Create your views here.


def index(request):
    return render(request, "index.html")


def hello(request):
    form = CusForm(request.POST)
    abc = {'form':form}
    if request.method == 'POST' and form.is_valid():
        data=form.cleaned_data
        ready_form = form.save()
    return render(request, 'main/index.html', abc)


def user_login(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data['login'], password=data['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('main:profile')
                else:
                    return HttpResponse('Авторизация провалена. Повторите попытку')
            else:
                return HttpResponse('Введены некорректные данные.')
    else:
        form = UserForm()
    return render(request, 'main/login.html', {'form': form})

''' https://pocoz.gitbooks.io/django-v-primerah/content/glava-4-sozdanie-social-website/ispolzovanie-django-authentication-framework/sozdanie-log-in-view.html'''


@login_required
def profile(request):
    return render(request, 'main/profile.html')


class LogoutView(LoginRequiredMixin, LogoutView):
    template_name = 'main/logout.html'

class RegisterUserView(CreateView):
    model = CustomUser
    template_name = 'main/register_user.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('main:register_done')


class RegisterDoneView(TemplateView):
    template_name = 'main/register_done.html'


@login_required
def change_pass(request):
    if request.method == 'POST':
        passwords = request.POST
        user = request.user
        old_password = passwords['old_password']
        new_password1 = passwords['new_password1']
        new_password2 = passwords['new_password2']
        if check_password(old_password, user.password):
            if new_password1 == new_password2:
                user.set_password(new_password1)
                user.save()
                message = 'Ваш пароль успешно изменен.'
                return render(request, 'main/index.html', context={'message': message})
            else:
                error = 'Пароли не совпадают'
                return render(request, 'main/change_pass.html', context={'error': error})
    form = ChangePasswordForm()
    context = {'form': form}
    return render(request, 'main/change_pass.html', context)