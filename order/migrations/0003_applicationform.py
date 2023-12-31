# Generated by Django 4.2.6 on 2023-10-22 10:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('order', '0002_alter_order_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicationForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('specie', models.CharField(max_length=25, verbose_name='Вид')),
                ('breed', models.CharField(blank=True, max_length=50, null=True, verbose_name='Порода')),
                ('name', models.CharField(max_length=100, verbose_name='Кличка')),
                ('sex', models.CharField(choices=[('Female', 'Female'), ('Male', 'Male')], max_length=10, verbose_name='Пол')),
                ('birth_date', models.DateField(blank=True, null=True, verbose_name='Дата рождения')),
                ('microchip_number', models.PositiveIntegerField(blank=True, null=True, verbose_name='Номер чипа')),
                ('pedigree', models.FileField(blank=True, null=True, upload_to='', verbose_name='Родословная')),
                ('extra_information', models.TextField(blank=True, null=True, verbose_name='Дополнительная информация')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Владелец')),
            ],
        ),
    ]
