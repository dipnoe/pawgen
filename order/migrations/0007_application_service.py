# Generated by Django 4.2.6 on 2023-10-23 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_category_description'),
        ('order', '0006_alter_application_options_application_create_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='service',
            field=models.ManyToManyField(to='main.service', verbose_name='услуга'),
        ),
    ]
