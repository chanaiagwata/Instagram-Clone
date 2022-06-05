from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path(r'', views.main, name = 'mainpage'),
    path(r'index/', views.index, name = 'indexpage')
]