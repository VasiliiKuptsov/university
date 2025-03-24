from django.urls import path
from rest_framework.permissions import AllowAny

from users.apps import UsersConfig
from rest_framework.routers import SimpleRouter

from users.views import PaymentViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from users.views import UserCreateAPIView

app_name = UsersConfig.name

router = SimpleRouter()
router.register(r"payment", PaymentViewSet, basename="payment")

urlpatterns = [
    path(
        "register/",
        UserCreateAPIView.as_view(permission_classes=(AllowAny,)),
        name="register",
    ),
    path(
        "token/",
        TokenObtainPairView.as_view(permission_classes=(AllowAny,)),
        name="token_obtain_pair",
    ),
    path(
        "token/refresh/",
        TokenRefreshView.as_view(permission_classes=(AllowAny,)),
        name="token_refresh",
    ),
]

urlpatterns += router.urls
