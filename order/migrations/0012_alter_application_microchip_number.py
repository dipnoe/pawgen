# Generated by Django 4.2.6 on 2023-10-24 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0011_application_is_submitted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='microchip_number',
            field=models.CharField(blank=True, max_length=15, null=True, unique=True, verbose_name='Номер чипа'),
        ),
    ]
