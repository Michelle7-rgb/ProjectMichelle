from django.urls import path
from .views import  login, register, logout_view,profil

urlpatterns = [
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('logout/', logout_view, name='logout'),
    path('p/', profil, name='tenant_profile'),
]