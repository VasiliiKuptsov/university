from django.contrib import admin
from materials.models import Course, Lesson, Subscription


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ["pk", "name", "description", "image"]


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ["pk", "name", "description", "video", "image", "course"]


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ["pk", "user", "course", "is_subscribe"]
