from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .choices import fiyat_choices, oda_choices, bolge_choices, kategori_choices

from .models import Ilan

def index(request):
  ilanlar = Ilan.objects.order_by('-liste_tarihi').filter(yayinlandi=True)

  paginator = Paginator(ilanlar, 6)
  page = request.GET.get('page')
  paged_listings = paginator.get_page(page)

  context = {
    'ilanlar': paged_listings
  }

  return render(request, 'ilanlar/ilanlar.html', context)

def ilan(request, ilan_id):
  ilan = get_object_or_404(Ilan, pk=ilan_id)

  context = {
    'ilan': ilan
  }

  return render(request, 'ilanlar/ilan.html', context)

def arama(request):
  queryset_list = Ilan.objects.order_by('-liste_tarihi')

  # AnahtarKelimeler
  if 'anahtarkelime' in request.GET:
    anahtarkelime = request.GET['anahtarkelime']
    if anahtarkelime:
      queryset_list = queryset_list.filter(aciklama__icontains=anahtarkelime)

  # Sehir
  if 'sehir' in request.GET:
    sehir = request.GET['sehir']
    if sehir:
      queryset_list = queryset_list.filter(sehir__iexact=sehir)

  # Bolge
  if 'bolge' in request.GET:
    bolge = request.GET['bolge']
    if bolge:
      queryset_list = queryset_list.filter(bolge__iexact=bolge)

  # oda
  if 'oda' in request.GET:
    oda = request.GET['oda']
    if oda:
      queryset_list = queryset_list.filter(oda__lte=oda)
  # Kategori
  if 'kategori' in request.GET:
    kategori = request.GET['kategori']
    if kategori:
      queryset_list = queryset_list.filter(kategori__iexact=kategori)
  # Fiyat
  if 'fiyat' in request.GET:
    fiyat = request.GET['fiyat']
    if fiyat:
      queryset_list = queryset_list.filter(fiyat__lte=fiyat)

  context = {
    'bolge_choices': bolge_choices,
    'oda_choices': oda_choices,
    'kategori_choices' : kategori_choices,
    'fiyat_choices': fiyat_choices,
    'ilanlar': queryset_list,
    'degerler': request.GET
  }

  return render(request, 'ilanlar/arama.html', context)