

from rest_framework.serializers import ModelSerializer, SerializerMethodField
from materials.models import Course, Lesson, Subscription
from rest_framework import serializers
from materials.validators import YouTubeValidator

class LessonSerializer(ModelSerializer):
    validators = [YouTubeValidator(field="url_video")]
   # course = CourseSerializer()
    class Meta:
        model = Lesson
        fields = '__all__'





class CourseSerializer(ModelSerializer):
    #count_lessons = serializers.SerializerMethodField(read_only=True)
    #set_lessons = LessonSerializer(many=True, source='course')
    #lessons = serializers.SerializerMethodField()
    lessons = LessonSerializer(many=True, read_only=True, source='lesson_set')
    #def get_lessons(self,course):
     #   return [lesson.name for lesson in Lesson.objects.filter(course=course)]



    class Meta:
        model = Course
        fields = '__all__'

        #def get_count_lessons(self, course):
         #   return Lesson.objects.filter(course=course).count()

        #def create(self, validated_data):
         #   lesson = validated_data.pop('set_lessons')
          #  course = Course.objects.create(**validated_data)
           # for lesson in lesson:
            #    Lesson.objects.create(course=course, **lesson)
             #   return course


class CourseDitailSerializer(ModelSerializer):
    lessons_count = serializers.SerializerMethodField(read_only=True)
    #set_lessons = LessonSerializer(many=True, source='course')
    subscription = serializers.SerializerMethodField(read_only=True)
    lessons = LessonSerializer(many=True, read_only=True, source='lesson_set')
    def get_lessons_count(self, course):
        return Lesson.objects.filter(course=course).count()

    def get_subscription(self, course):
        user = self.context['request'].user
        return Subscription.objects.all().filter(user=user).filter(course=course).exist()

    class Meta:
        model = Course
        fields = ('name', 'description', 'lessons_count', 'lessons', 'subscription')


class SubscriptionSerializer(ModelSerializer):
    class Meta:
        model = Subscription
        fields = ('is_subscribe',)


