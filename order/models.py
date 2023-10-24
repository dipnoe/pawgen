from django.db import models
from django.db.models import Sum

from main.models import Service
from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Application(models.Model):
    SEX = [
        ('Female', 'Female'),
        ('Male', 'Male'),
    ]

    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Владелец')
    specie = models.CharField(max_length=25, verbose_name='Вид')
    breed = models.CharField(max_length=50, verbose_name='Порода', **NULLABLE)
    name = models.CharField(max_length=100, verbose_name='Кличка')
    sex = models.CharField(max_length=10, choices=SEX, verbose_name='Пол')
    birth_date = models.DateField(verbose_name='Дата рождения', **NULLABLE)
    microchip_number = models.PositiveIntegerField(verbose_name='Номер чипа', unique=True, **NULLABLE)
    pedigree = models.FileField(verbose_name='Родословная', **NULLABLE)
    extra_information = models.TextField(verbose_name='Дополнительная информация', **NULLABLE)
    create_date = models.DateTimeField(verbose_name='дата создания', auto_now_add=True)
    service = models.ManyToManyField(Service, verbose_name='услуга')

    def __str__(self):
        return f'{self.specie} {self.name} пользователя {self.owner}'

    def full_price(self):
        total_price = self.service.aggregate(total_price=Sum('price'))['total_price']
        return total_price if total_price is not None else 0

    def status(self):
        order = Order.objects.get(application_id=self.pk)
        return order['status']

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'
        ordering = ['-create_date']


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
    application = models.ForeignKey(Application, on_delete=models.CASCADE, verbose_name='заявка', **NULLABLE)

    def __str__(self):
        return f'Заказ {self.pk} пользователя {self.user}'

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        ordering = ['-create_date']
