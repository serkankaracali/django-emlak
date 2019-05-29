from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import Baglanti

def baglanti(request):
  if request.method == 'POST':
    ilan_id = request.POST['ilan_id']
    ilan = request.POST['ilan']
    isim = request.POST['isim']
    email = request.POST['email']
    telefon = request.POST['telefon']
    mesaj = request.POST['mesaj']
    user_id = request.POST['user_id']
    emlakci_email = request.POST['emlakci_email']

    #  Check if user has made inquiry already
    if request.user.is_authenticated:
      user_id = request.user.id
      baglanti_var = Baglanti.objects.all().filter(ilan_id=ilan_id, user_id=user_id)
      if baglanti_var:
        messages.error(request, 'Bu ilan için zaten bir soruşturma yaptınız.')
        return redirect('/ilanlar/'+ilan_id)

    baglanti = Baglanti(ilan=ilan, ilan_id=ilan_id, isim=isim, email=email, telefon=telefon, mesaj=mesaj, user_id=user_id )

    baglanti.save()

    # Send email
    # send_mail(
    #   'Property Listing Inquiry',
    #   'There has been an inquiry for ' + listing + '. Sign into the admin panel for more info',
    #   'traversy.brad@gmail.com',
    #   [realtor_email, 'techguyinfo@gmail.com'],
    #   fail_silently=False
    # )

    messages.success(request, 'İsteğiniz gönderildi, bir emlakçı yakında size geri dönecek.')
    return redirect('/ilanlar/'+ilan_id)
