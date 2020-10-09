from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="index"),
    path('overview', views.home2, name="admin")
]

