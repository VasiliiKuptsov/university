# Generated by Django 5.1.7 on 2025-03-10 21:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Course",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="введите название курса",
                        max_length=200,
                        verbose_name="наименование курса",
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        help_text="введите изображение курса",
                        null=True,
                        upload_to="",
                        verbose_name="изображение",
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True,
                        help_text="опишите курса",
                        null=True,
                        verbose_name="описание курса",
                    ),
                ),
            ],
            options={
                "verbose_name": "Курс",
                "verbose_name_plural": "Курсы",
            },
        ),
        migrations.CreateModel(
            name="Lesson",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="введите название урока",
                        max_length=200,
                        verbose_name="наименование",
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True,
                        help_text="опищите урок",
                        null=True,
                        verbose_name="описание",
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        help_text="введите плакат урока",
                        null=True,
                        upload_to="",
                        verbose_name="изображение",
                    ),
                ),
                (
                    "video",
                    models.ImageField(
                        blank=True,
                        help_text="введите видео урока",
                        null=True,
                        upload_to="",
                        verbose_name="изображение",
                    ),
                ),
                (
                    "course",
                    models.ForeignKey(
                        blank=True,
                        help_text="введите курс",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="materials",
                        to="materials.course",
                        verbose_name="курс",
                    ),
                ),
            ],
            options={
                "verbose_name": "Курс",
                "verbose_name_plural": "Курсы",
            },
        ),
    ]
