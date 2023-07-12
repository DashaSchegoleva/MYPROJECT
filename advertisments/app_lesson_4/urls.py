from django.urls import path
from .views import index
urlpatterns = [
    path('lesson_4/', index),
]
#python manage.py runserver 80 - запуск сервера без :800
