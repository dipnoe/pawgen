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
   - is_active (BooleanField): Indicates whether the user is active or not, default is True.
   """
    username = None
    email = models.EmailField(max_length=50, verbose_name='почта', unique=True)
    phone = models.PositiveIntegerField(verbose_name='телефон', unique=True)
    first_name = models.CharField(max_length=50, verbose_name='Имя')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', **NULLABLE)
    city = models.CharField(max_length=50, verbose_name='город', **NULLABLE)
    last_login = models.DateField(verbose_name='дата последнего входа', auto_now=True, **NULLABLE)

    is_active = models.BooleanField(verbose_name='активный', default=True)

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
