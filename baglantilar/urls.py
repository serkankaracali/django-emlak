from django.urls import path

from . import views

urlpatterns = [
  path('baglanti', views.baglanti, name='baglanti')
]