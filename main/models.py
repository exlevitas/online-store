from django.contrib.auth.models import AbstractUser, User
from django.db import models
from django.dispatch import Signal
# from .utilities import send_activation_notification
# Create your models here.


class Customers(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=50, db_index=True, unique=True)
    rassilka = models.BooleanField(default=True, verbose_name='Согласны ли вы получать рассылку?')

    def __str__(self):
        return 'Пользователь %s' % (self.name)


class DataModelUser(models.Model):
    login = models.CharField(unique=True, max_length=50)
    password = models.CharField(max_length=100)



# class AdvUser(models.Model):
#     is_activated = models.BooleanField(default=True)
#     user = models.OneToOneField(User, on_delete=models.CASCADE)

# user_registrated = Signal(providing_args=['instance'])
#
# def user_registrated_dispatcher(sender, **kwargs):
#     send_activation_notification(kwargs['instance'])
#
# user_registrated.connect(user_registrated_dispatcher)


class CustomUser(AbstractUser):
    pass


