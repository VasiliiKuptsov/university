from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from materials.models import Lesson, Course, Subscription
from users.models import User


class CourseTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email='admin@pro.com')
        self.course = Course.objects.create(name='test/letter1', description='test test', owner=self.user)
        self.lesson = Lesson.objects.create(name='Letter1', description='Letter1 test', course=self.course)
        self.client.force_authenticate(user=self.user)

    def test_course_retrieve(self):
        url = reverse('materials:course-detail', args=(self.course.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data.get('name'), self.course.name
        )

    def test_course_create(self):
        url = reverse('materials:course-list')
        data = {

            'name': 'test',
            'description': 'letter1'
        }
        response = self.client.post(url, data)
        self.assertEqual(
            response.status_code, status.HTTP_201_CREATED
        )
        self.assertEqual(
            Course.objects.all().count(), 2
        )


    def test_course_delete(self):
        url = reverse('materials:course-detail', args=(self.course.pk,))

        response = self.client.delete(url)
        self.assertEqual(
            response.status_code, status.HTTP_204_NO_CONTENT
        )
        self.assertEqual(
            Course.objects.all().count(), 0
        )


class LessonTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email='admin@pro.com')
        self.course = Course.objects.create(name='test/letter1', description='Test test', owner=self.user)
        self.lesson = Lesson.objects.create(name='Letter1', description='Letter1 test', course=self.course,
                                            owner=self.user)
        self.client.force_authenticate(user=self.user)

    def test_lesson_retrieve(self):
        url = reverse('materials:lessons_get', args=(self.lesson.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data.get('name'), self.lesson.name
        )

    def test_lesson_create(self):
        url = reverse('materials:lessons_create')
        data = {
            'name': 'letter',
            'description': 'test'
        }
        response = self.client.post(url, data)
        self.assertEqual(
            response.status_code, status.HTTP_201_CREATED
        )
        self.assertEqual(
            Lesson.objects.all().count(), 2
        )

    def test_lesson_update(self):
        url = reverse('materials:lessons_update', args=(self.lesson.pk,))
        data = {
            'name': 'letter 2'
        }
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data.get('name'), 'letter 2'
        )

    def test_lesson_delete(self):
        url = reverse('materials:lessons_delete', args=(self.lesson.pk,))

        response = self.client.delete(url)
        self.assertEqual(
            response.status_code, status.HTTP_204_NO_CONTENT
        )
        self.assertEqual(
            Lesson.objects.all().count(), 0
        )

    def test_lesson_list(self):
        url = reverse('materials:lessons_list')
        response = self.client.get(url)
        data = response.json()
        result = {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {
                    "id": self.lesson.pk,
                    "name": self.lesson.name,
                    "description": self.lesson.description,
                    "image": None,
                    "video": None,
                    "course": self.course.pk,
                    "owner": self.user.pk
                }]}
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data, result
        )


class SubscriptionTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email='admin@pro.com')
        self.course = Course.objects.create(name='Test/letter1', description='Test test', owner=self.user)
        self.lesson = Lesson.objects.create(name='letter1', description='letter1 test', course=self.course,
                                            owner=self.user)
        self.client.force_authenticate(user=self.user)

    def test_subscription_create(self):
        url = reverse('materials:subscription_create')
        data = {
            'user': self.user,
            'course': self.course.pk
        }
        response = self.client.post(url, data)
        data = response.json()
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data, {'message': 'Подписка добавлена'}
        )

    def test_subscription_delete(self):
        self.subscription = Subscription.objects.create(user=self.user, course=self.course)
        url = reverse('materials:subscription_create')
        data = {
            'user': self.user,
            'course': self.course.pk
        }
        response = self.client.post(url, data)
        data = response.json()
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data, {'message': 'Подписка удалена'}
        )