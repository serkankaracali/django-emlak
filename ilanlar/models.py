from django.db import models
from datetime import datetime
from emlakcilar.models import Emlakci

class Ilan(models.Model):
  emlakci = models.ForeignKey(Emlakci, on_delete=models.DO_NOTHING)
  baslik = models.CharField(max_length=200)
  adres = models.CharField(max_length=200)
  sehir = models.CharField(max_length=100)
  bolge = models.CharField(max_length=100)
  zipcode = models.CharField(max_length=20)
  kategori = models.CharField(max_length=100)
  aciklama = models.TextField(blank=True)
  fiyat = models.IntegerField()
  yatakodasi = models.IntegerField()
  banyo = models.IntegerField()
  garaj = models.IntegerField(default=0)
  metrekare = models.IntegerField()
  oda = models.CharField(max_length=50)
  foto_ana = models.ImageField(upload_to='photos/%Y/%m/%d/')
  foto_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  foto_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  foto_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  foto_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  foto_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  foto_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  yayinlandi = models.BooleanField(default=True)
  liste_tarihi = models.DateTimeField(default=datetime.now, blank=True)
  def __str__(self):
    return self.baslik