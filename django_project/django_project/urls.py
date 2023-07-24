from django.contrib import admin
from django.urls import path
# from apps import views
from django_project.apps import views

views
urlpatterns = [
    path('', views.index),
    path('admin/', admin.site.urls),
]
