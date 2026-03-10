from django.urls import path
from .views import mes_favoris

urlpatterns = [
    path("fa/", mes_favoris, name="tenant_favorites"),
]
