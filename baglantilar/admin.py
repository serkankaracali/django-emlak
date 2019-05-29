from django.contrib import admin

from .models import Baglanti

class BaglantiAdmin(admin.ModelAdmin):
  liste_ekrani = ('id', 'isim', 'ilan', 'email', 'baglanti_zamani')
  liste_ekrani_links = ('id', 'isim')
  arama_alani = ('isim', 'email', 'ilan')
  her_sayfa_liste = 25

admin.site.register(Baglanti, BaglantiAdmin)