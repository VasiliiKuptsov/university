from django.db import models
from config.settings import AUTH_USER_MODEL
NULLABLE = {'blank': True, 'null': True}



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
    video = models.URLField(
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
        

class Subscription(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='пользователь')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='курс')
    is_subscribe = models.BooleanField(default=False, verbose_name="подписка")

    def __str__(self):
        return f'{self.user} - {self.course}'

    class Meta:
        verbose_name = 'подписка'
        verbose_name_plural = 'подписки'






