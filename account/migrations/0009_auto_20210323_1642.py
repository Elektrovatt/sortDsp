# Generated by Django 3.1.4 on 2021-03-23 16:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0008_auto_20210307_1147'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profileusermodel',
            options={'ordering': ('-value2',), 'verbose_name': 'Профиль', 'verbose_name_plural': 'Профили для выбора Форм'},
        ),
    ]
