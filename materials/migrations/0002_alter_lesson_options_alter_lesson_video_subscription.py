# Generated by Django 4.2.5 on 2025-03-17 11:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('materials', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lesson',
            options={'verbose_name': 'Урок', 'verbose_name_plural': 'Уроки'},
        ),
        migrations.AlterField(
            model_name='lesson',
            name='video',
            field=models.URLField(blank=True, help_text='введите видео урока', null=True, verbose_name='видео'),
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_subscribe', models.BooleanField(default=False, verbose_name='подписка')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='курс', to='materials.course')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='пользователь', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'подписка',
                'verbose_name_plural': 'подписки',
            },
        ),
    ]
