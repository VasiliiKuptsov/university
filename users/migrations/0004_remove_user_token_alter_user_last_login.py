# Generated by Django 4.2.5 on 2025-03-17 12:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_user_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='token',
        ),
        migrations.AlterField(
            model_name='user',
            name='last_login',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now, null=True, verbose_name='Время последнего посещения'),
        ),
    ]
