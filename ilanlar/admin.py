from django.contrib import admin

from .models import Ilan

class IlanAdmin(admin.ModelAdmin):
  liste_ekrani = ('id', 'tbaslik', 'yayinlandi', 'fiyat', 'liste_tarihi', 'emlakci')
  liste_ekrani_links = ('id', 'baslik')
  liste_filter = ('emlakci',)
  liste_duzen = ('yayinlandi',)
  arama_alani = ('baslik', 'aciklama', 'adres', 'sehir', 'bolge', 'zipcode', 'fiyat')
  her_sayfa_liste = 25

admin.site.register(Ilan, IlanAdmin)