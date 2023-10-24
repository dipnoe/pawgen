from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'blank': True, 'null': True}


# Create your models here.
class User(AbstractUser):
    """
    Custom user model representing a user in the system.

    Fields:
    - email (EmailField): Email address of the user. Used for authentication and must be unique.
    - phone (PositiveIntegerField): Phone number of the user, also unique.
    - first_name (CharField): First name of the user.
    - last_name (CharField): Last name of the user.
    - avatar (ImageField): User's avatar image. Can be NULL.
    - city (CharField): City where the user is located. Can be NULL.
    - last_login (DateField): Date of the last login. Automatically updated. Can be NULL.
    - approval_code (CharField): Code for email approval, unique. Can be NULL.
    - is_active (BooleanField): Indicates whether the user is active or not, default is True.
    - is_approved (BooleanField): Indicates whether the user is approved via email, default is False.
   """
    username = None
    email = models.EmailField(max_length=50, verbose_name='почта', unique=True)
    phone = models.PositiveIntegerField(verbose_name='телефон', unique=True)
    first_name = models.CharField(max_length=50, verbose_name='Имя')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', **NULLABLE)
    city = models.CharField(max_length=50, verbose_name='город', **NULLABLE)
    last_login = models.DateField(verbose_name='дата последнего входа', auto_now=True, **NULLABLE)
    approval_code = models.CharField(max_length=255, verbose_name='код подтверждения почты', unique=True, **NULLABLE)
    is_active = models.BooleanField(verbose_name='активный', default=True)
    is_approved = models.BooleanField(verbose_name='подтвержденный через почту', default=False)

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
