from django.db import models

from users.models import User


class Course(models.Model):
    name = models.CharField(
        max_length=200,
        verbose_name="наименование курса",
        help_text="введите название курса",
    )
    image = models.ImageField(
        #upload_to="products/photo",
        blank=True,
        null=True,
        verbose_name="изображение",
        help_text="введите изображение курса",
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name="описание курса",
        help_text="опишите курса",
    )

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"


class Lesson(models.Model):
    name = models.CharField(
        max_length=200,
        verbose_name="наименование",
        help_text="введите название урока",
    )

    description = models.TextField(
        blank=True, null=True, verbose_name="описание", help_text="опищите урок",
    )
    image = models.ImageField(
        #upload_to="products/photo",
        blank=True,
        null=True,
        verbose_name="изображение",
        help_text="введите плакат урока",
    )
    video = models.ImageField(
        # upload_to="products/photo",
        blank=True,
        null=True,
        verbose_name="видео",
        help_text="введите видео урока",
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.SET_NULL,
        verbose_name="курс",
        help_text="введите курс",
        blank=True,
        null=True,
        related_name='materials',
    )


    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"
        








'''
    price = models.IntegerField(
        blank=True,
        null=True,
        verbose_name="цена за покупку",
        help_text="укахите цену продукта",
    )

    updated_at = models.DateField(
        blank=True,
        null=True,
        verbose_name="дата последнего изменения",
        help_text="введите последнего изменения продукта",
    )

    views_counter = models.PositiveIntegerField(
        verbose_name='Счетчик просмотров',
        help_text='Укахите количество просмотров',
        default=0,
    )

    owner = models.ForeignKey(
        User,
        verbose_name='Купец',
        help_text='Укажите продавца товараэ',
        blank=True, null=True,
        on_delete=models.SET_NULL,
    )

    publication = models.BooleanField(
        default=False,
        verbose_name='Опубликовано',
    )

'''