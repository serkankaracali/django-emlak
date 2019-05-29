from django.shortcuts import render
from django.http import HttpResponse
from ilanlar.choices import fiyat_choices, oda_choices, bolge_choices, kategori_choices

from ilanlar.models import Ilan
from emlakcilar.models import Emlakci

def index(request):
    ilanlar = Ilan.objects.order_by('-liste_tarihi').filter(yayinlandi=True)[:3]

    context = {
        'ilanlar': ilanlar,
        'bolge_choices': bolge_choices,
        'oda_choices': oda_choices,
        'kategori_choices': kategori_choices,
        'fiyat_choices': fiyat_choices
    }

    return render(request, 'sayfalar/index.html', context)


def hakkinda(request):
    # emlakcilari al
    emlakcilar = Emlakci.objects.order_by('-kira_tarihi')

    #  MVP al
    mvp_emlakcilar = Emlakci.objects.all().filter(is_mvp=True)

    context = {
        'emlakcilar': emlakcilar,
        'mvp_emlakcilar': mvp_emlakcilar
    }

    return render(request, 'sayfalar/hakkinda.html', context)