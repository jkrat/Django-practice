from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('submit', views.process, name="process"),
    path('success', views.success, name="success")
]