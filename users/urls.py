""" Определяет схемы URL для пользователей """
from django.conf.urls import url
from django.contrib.auth.views import login

from . import views

urlpatterns = [
    # Страница входа
    url(r'^login/$', login, {'template_name': 'users/login.html'},
        name='login'),
]
