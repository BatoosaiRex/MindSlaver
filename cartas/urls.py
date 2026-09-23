from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from .views import CartaViewSet

router = DefaultRouter()
router.register(r'cartas', CartaViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('users/login/', obtain_auth_token, name='api_token_auth'), # <--- Agregamos esta línea
]