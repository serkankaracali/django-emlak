from django.db import models
from datetime import datetime

class Emlakci(models.Model):
  isim = models.CharField(max_length=200)
  foto = models.ImageField(upload_to='photos/%Y/%m/%d/')
  aciklama = models.TextField(blank=True)
  telefon = models.CharField(max_length=20)
  email = models.CharField(max_length=50)
  is_mvp = models.BooleanField(default=False)
  kira_tarihi = models.DateTimeField(default=datetime.now, blank=True)
  def __str__(self):
    return self.isim