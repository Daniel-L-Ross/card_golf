
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from rest_framework import routers
from card_golfapi.views import register_user, login_user

router = routers.DefaultRouter(trailing_slash=False)

urlpatterns = [
    path('register', register_user),
    path('login', login_user),
    path('', include(router.urls)),
    path('api-ath', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
]
