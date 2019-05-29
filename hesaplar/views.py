from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from baglantilar.models import Baglanti

def kayit(request):
  if request.method == 'POST':
    # Form değerlerini al
    ilk_isim = request.POST['ilk_isim']
    soy_isim = request.POST['soy_isim']
    kullaniciadi = request.POST['kullaniciadi']
    email = request.POST['email']
    sifre = request.POST['sifre']
    sifre2 = request.POST['sifre2']

    # Şifre kontrolü
    if sifre == sifre2:
      # Kullanıcı adı kontrolu
      if User.objects.filter(username=kullaniciadi).exists():
        messages.error(request, 'Bu kullanıcı adı alınmış')
        return redirect('kayit')
      else:
        if User.objects.filter(email=email).exists():
          messages.error(request, 'Bu email hesabı kullanılıyor')
          return redirect('kayit')
        else:
          # Looks good
          user = User.objects.create_user(username=kullaniciadi, password=sifre,email=email, first_name=ilk_isim, last_name=soy_isim)
          # Login after register
          # auth.login(request, user)
          # messages.success(request, 'You are now logged in')
          # return redirect('index')
          user.save()
          messages.success(request, 'Kayıt olundu şimdi giriş yapabilirsiniz')
          return redirect('giris')
    else:
      messages.error(request, 'Şifreler eşleşmiyor')
      return redirect('kayit')
  else:
    return render(request, 'hesaplar/kayit.html')

def giris(request):
  if request.method == 'POST':
    kullaniciadi = request.POST['kullaniciadi']
    sifre = request.POST['sifre']
    user = auth.authenticate(username=kullaniciadi, password=sifre)

    if user is not None:
      auth.login(request, user)
      messages.success(request, 'Giriş yapıldı')
      return redirect('panel')
    else:
      messages.error(request, 'Geçersiz bilgiler')
      return redirect('giris')
  else:
    return render(request, 'hesaplar/giris.html')

def cikis(request):
  if request.method == 'POST':
    auth.logout(request)
    messages.success(request, 'Çıkış yapıldı')
    return redirect('index')

def panel(request):
  user_baglantilar = Baglanti.objects.order_by('-baglanti_zamani').filter(user_id=request.user.id)

  context = {
    'baglantilar': user_baglantilar
  }
  return render(request, 'hesaplar/panel.html', context)