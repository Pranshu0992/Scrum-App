from django.conf.urls import url

from .api import ListAPI, CardAPI

urlpatterns = [
    url(r'lists', ListAPI.as_view()),
    url(r'card', CardAPI.as_view())
]