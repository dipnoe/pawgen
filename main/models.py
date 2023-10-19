from django.db import models

NULLABLE = {'blank': True, 'null': True}


# Create your models here.
class Category(models.Model):
    """
    Model representing a category.

    Fields:
    - name (CharField): The name of the category.
    """
    name = models.CharField(max_length=100, verbose_name='Категория')
    description = models.TextField(verbose_name='Описание', **NULLABLE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Service(models.Model):
    """
    Model representing a service.

    Fields:
    - name (CharField): The name of the service.
    - price (PositiveSmallIntegerField): The price of the service.
    - description (TextField): Description of the service. Can be NULL.
    - is_available (BooleanField): Indicates whether the service is available.
    - category (ForeignKey): The category to which the service belongs.
    """
    name = models.CharField(max_length=100, verbose_name='Услуга', unique=True)
    price = models.PositiveSmallIntegerField(verbose_name='Цена')
    description = models.TextField(verbose_name='Описание', **NULLABLE)
    is_available = models.BooleanField(default=True, verbose_name='доступность')

    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'
