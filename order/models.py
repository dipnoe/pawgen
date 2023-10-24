from django.db import models
from django.db.models import Sum

from main.models import Service
from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Application(models.Model):
    """
    Model representing an application for pet services.

    Fields:
    - owner (ForeignKey): The user who owns the pet.
    - specie (CharField): The species of the pet.
    - breed (CharField): The breed of the pet (optional).
    - name (CharField): The name of the pet.
    - sex (CharField with choices): The sex of the pet.
    - birth_date (DateField): The date of birth of the pet (optional).
    - microchip_number (CharField): The microchip number of the pet (unique).
    - pedigree (FileField): The pedigree of the pet (optional).
    - extra_information (TextField): Additional information about the pet (optional).
    - create_date (DateTimeField): The date and time when the application was created (auto-generated).
    - service (ManyToManyField): The list of services associated with the application.
    - is_submitted (BooleanField): Indicates whether the application is submitted or not.

    Methods:
    - full_price(): Calculates the total price of services associated with the application.
    - status(): Retrieves the status of the associated order.

    Relationships:
    - User (owner): The user who owns the pet.
    - Service (service): The list of services associated with the application.
    - Order: The associated order, if any.
    """
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
    microchip_number = models.CharField(max_length=15, verbose_name='Номер чипа', unique=True, **NULLABLE)
    pedigree = models.FileField(verbose_name='Родословная', **NULLABLE)
    extra_information = models.TextField(verbose_name='Дополнительная информация', **NULLABLE)
    create_date = models.DateTimeField(verbose_name='дата создания', auto_now_add=True)
    service = models.ManyToManyField(Service, verbose_name='услуга')
    is_submitted = models.BooleanField(verbose_name='подтверждена', default=False)

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
    """
    Model representing an order for pet services.

    Fields:
    - service (ManyToManyField): The list of services in the order.
    - user (ForeignKey): The user who placed the order.
    - status (CharField with choices): The status of the order.
    - amount (PositiveSmallIntegerField): The total amount of the order.
    - create_date (DateTimeField): The date and time when the order was created (auto-generated).
    - modify_date (DateTimeField): The date and time when the order was last modified (auto-updated).
    - application (ForeignKey): The associated application (optional).

    Relationships:
    - Service (service): The list of services in the order.
    - User (user): The user who placed the order.
    - Application (application): The associated application, if any.

    Permissions:
    - "set_status": Permission to change the status of an order.
    """
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
        permissions = [
            (
                "set_status",
                "Can change status"
            )
        ]
