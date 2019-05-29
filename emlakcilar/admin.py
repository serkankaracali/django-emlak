from django.contrib import admin

from .models import Emlakci

class EmlakciAdmin(admin.ModelAdmin):
  liste_ekrani = ('id', 'isim', 'email', 'kira_tarihi')
  liste_ekrani_links = ('id', 'isim')
  arama_alani = ('isim',)
  her_sayfa_liste = 25

admin.site.register(Emlakci, EmlakciAdmin)