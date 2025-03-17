

from rest_framework.serializers import ModelSerializer, SerializerMethodField
from materials.models import Course, Lesson, Subscription
from rest_framework import serializers
from materials.validators import YouTubeValidator

class LessonSerializer(serializers.ModelSerializer):

    validators = [YouTubeValidator(field="url_video")]

    class Meta:
        model = Lesson
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    lessons = SerializerMethodField()
    lessons_set = LessonSerializer(many=True, read_only=True, source='course')
    lessons_count = serializers.SerializerMethodField(read_only=True)

    def get_lessons(self,course):
        return [lesson.name for lesson in Lesson.objects.filter(course=course)]
    def get_lessons_count(self, course):
        return Lesson.objects.filter(course=course).count()




    def get_lessons_set(self, validated_data):
        lesson = validated_data.pop('lessons_set')
        course = Course.objects.create(**validated_data)
        for lesson in lesson:
            Lesson.objects.create(course=course, **lesson)
            return course





    class Meta:
        model = Course
        fields = ['id', 'name', 'description', 'lessons_count', 'lessons_set','lessons']





class CourseDitailSerializer(serializers.ModelSerializer):
    lessons = SerializerMethodField()
    lessons_count = serializers.SerializerMethodField(read_only=True)

    subscription = serializers.SerializerMethodField(read_only=True)
    lessons_set = LessonSerializer(many=True, read_only=True, source='lesson_set')


    def get_lessons(self,course):
        return [lesson.name for lesson in Lesson.objects.filter(course=course)]

    def get_lessons_count(self, course):
        return Lesson.objects.filter(course=course).count()

    def get_subscription(self, course):
        user = self.context.get('request').user
        course = self.context.get('view').kwargs.get('pk')
        subscription = Subscription.objects.filter(user=user, course=course)
        if subscription.exists():
            return True
        else:
            return False

    class Meta:
        model = Course
        fields = ['id', 'name', 'description', 'lessons_count', 'lessons_set', 'lessons', 'subscription']






class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'


