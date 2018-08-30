from django.conf.urls import url
from django.views.generic import TemplateView


from .api import ListAPI, CardAPI


urlpatterns = [
    url(r'lists', ListAPI.as_view()), 
    url(r'cards', CardAPI.as_view()),
    url(r'^home', TemplateView.as_view(template_name="scrumboard/home.html")),
]