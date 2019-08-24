from django.conf.urls import url, include
from django.urls import path
from . import views
app_name="devconsole"
urlpatterns = [
    path('', views.index, name='index'),
]