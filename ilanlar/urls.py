from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='ilanlar'),
    path('<int:ilan_id>', views.ilan, name='ilan'),
    path('arama', views.arama, name='arama'),
]