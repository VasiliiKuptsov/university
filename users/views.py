from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import CreateAPIView
from users.models import Payment, User
from users.serializers import PaymentSerializer, UserSerializer



class PaymentViewSet(ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['payment_date', 'cost']
    search_fields = ['payment_course', 'payment_lesson','payment_method']







