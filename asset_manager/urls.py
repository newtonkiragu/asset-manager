from django.conf.urls import url
from django.urls import path

from asset_manager import views

urlpatterns = [
    url('^$', views.index, name='index'),
]
