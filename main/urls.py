import django
from django.urls import path
from . import views
from django.contrib.auth.views import login_required
from .views import index, user_login, login, LogoutView, RegisterDoneView, RegisterUserView
from django.conf import settings
from django.conf.urls.static import static

app_name='main'

urlpatterns = [
    path('', views.hello, name='hello'),
    path('login/', user_login, name='login'),
    path('profile/', views.profile, name='profile'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/done/', RegisterDoneView.as_view(), name='register_done'),
    path('register/', RegisterUserView.as_view(), name='register'),
    path('change_pass/', views.change_pass, name='change_pass'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)