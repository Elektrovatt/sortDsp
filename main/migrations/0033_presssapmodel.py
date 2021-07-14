# Generated by Django 3.2 on 2021-07-14 08:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0032_auto_20210713_0925'),
    ]

    operations = [
        migrations.CreateModel(
            name='PressSapModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateField(verbose_name='Дата')),
                ('name_form1', models.BooleanField(default=False, verbose_name='121')),
                ('name_form2', models.BooleanField(default=False, verbose_name='123')),
                ('name_form3', models.BooleanField(default=False, verbose_name='125')),
                ('name_form4', models.BooleanField(default=False, verbose_name='127')),
                ('name_form5', models.BooleanField(default=False, verbose_name='129')),
                ('name_form6', models.BooleanField(default=False, verbose_name='131')),
                ('name_form7', models.BooleanField(default=False, verbose_name='133')),
                ('name_form8', models.BooleanField(default=False, verbose_name='135')),
                ('name_form9', models.BooleanField(default=False, verbose_name='160')),
                ('name_form10', models.BooleanField(default=False, verbose_name='161')),
                ('name_form11', models.BooleanField(default=False, verbose_name='162')),
                ('name_form12', models.BooleanField(default=False, verbose_name='163')),
                ('name_form13', models.BooleanField(default=False, verbose_name='164')),
                ('name_form14', models.BooleanField(default=False, verbose_name='171')),
                ('name_form15', models.BooleanField(default=False, verbose_name='173')),
                ('name_form16', models.BooleanField(default=False, verbose_name='175')),
                ('name_form17', models.BooleanField(default=False, verbose_name='177')),
                ('name_form18', models.BooleanField(default=False, verbose_name='179')),
                ('name_form19', models.BooleanField(default=False, verbose_name='181')),
                ('name_form20', models.BooleanField(default=False, verbose_name='183')),
                ('name_form21', models.BooleanField(default=False, verbose_name='122')),
                ('name_form22', models.BooleanField(default=False, verbose_name='124')),
                ('name_form23', models.BooleanField(default=False, verbose_name='126')),
                ('name_form24', models.BooleanField(default=False, verbose_name='128')),
                ('name_form25', models.BooleanField(default=False, verbose_name='130')),
                ('name_form26', models.BooleanField(default=False, verbose_name='132')),
                ('name_form27', models.BooleanField(default=False, verbose_name='134')),
                ('name_form28', models.BooleanField(default=False, verbose_name='136')),
                ('name_form29', models.BooleanField(default=False, verbose_name='172')),
                ('name_form30', models.BooleanField(default=False, verbose_name='174')),
                ('name_form31', models.BooleanField(default=False, verbose_name='176')),
                ('name_form32', models.BooleanField(default=False, verbose_name='178')),
                ('name_form33', models.BooleanField(default=False, verbose_name='180')),
                ('name_form34', models.BooleanField(default=False, verbose_name='182')),
                ('name_form35', models.BooleanField(default=False, verbose_name='184')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Владелец записи, пользователь')),
            ],
            options={
                'verbose_name': 'поля',
                'verbose_name_plural': 'Пресс - Состояние форсунок САП',
                'ordering': ('-date_created',),
            },
        ),
    ]