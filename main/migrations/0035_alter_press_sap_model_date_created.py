# Generated by Django 3.2 on 2021-07-14 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0034_auto_20210714_0806'),
    ]

    operations = [
        migrations.AlterField(
            model_name='press_sap_model',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата'),
        ),
    ]
