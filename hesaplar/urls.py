from django.urls import path

from . import views

urlpatterns = [
    path('giris', views.giris, name='giris'),
    path('kayit', views.kayit, name='kayit'),
    path('cikis', views.cikis, name='cikis'),
    path('panel', views.panel, name='panel')
]