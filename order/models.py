from django.db import models

from main.models import Service
from users.models import User


# Create your models here.
class Order(models.Model):
    STATUS = [
        ('Created', 'Создан'),
        ('Submitted', 'Подтвержден'),
        ('Paid', 'Оплачен'),
        ('Completed', 'Завершен'),
    ]
    service = models.ManyToManyField(Service, verbose_name='услуга')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь')
    status = models.CharField(max_length=15, choices=STATUS, default=STATUS[0][0], verbose_name='статус')
    amount = models.PositiveSmallIntegerField(verbose_name='сумма')
    create_date = models.DateTimeField(verbose_name='дата создания', auto_now_add=True)
    modify_date = models.DateTimeField(verbose_name='дата изменения', auto_now=True)

    def __str__(self):
        return f'Заказ {self.pk} пользователя {self.user}'

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
