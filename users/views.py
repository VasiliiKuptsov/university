from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, generics
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import AllowAny

from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import CreateAPIView
from users.models import Payment, User
from users.serializers import PaymentSerializer, UserSerializer


class PaymentViewSet(ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    ordering_fields = ["payment_date", "cost"]
    search_fields = ["payment_course", "payment_lesson", "payment_method"]

class PaymentListAPIView(generics.ListAPIView):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()

    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['payment_lesson', 'payment_course', 'payment_method']
    ordering_fields = ['-payment_date']

class UserCreateAPIView(generics.CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        user = serializer.save()
        user.set_password(user.password)
        user.save()
