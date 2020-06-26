from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.conf.urls import url
from .views import UserViewsets, CustomObtainTokenPairView, SignUpView
from rest_framework_simplejwt.views import (TokenRefreshView, TokenVerifyView)


app_name = 'user'

router = DefaultRouter()
router.register('users', UserViewsets)

urlpatterns = [
    path('', include(router.urls)),
    path('sign_up/', SignUpView.as_view(), name='sign_up'),
    path('login/', CustomObtainTokenPairView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='refresh-token'),
    path('token/verify/', TokenVerifyView.as_view(), name='verify-token'),
]
