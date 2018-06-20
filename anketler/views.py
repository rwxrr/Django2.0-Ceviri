from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Secim, Soru


class AnasayfaView(generic.ListView):
    template_name = 'anketler/anasayfa.html'
    context_object_name = 'son_sorular_listesi'

    def get_queryset(self):
        # Henüz yayınlanmamış sorular hariç.
        return Soru.objects.filter(yayim_tarihi__lte=timezone.now())


class DetayView(generic.DetailView):
    model = Soru
    template_name = 'anketler/detay.html'


class SonuclarView(generic.DetailView):
    model = Soru
    template_name = 'anketler/sonuclar.html'


def oy(request, soru_id):
    soru = get_object_or_404(Soru, pk=soru_id)
    try:
        secim_secildi = soru.secim_set.get(pk=request.POST['secim'])
    except (KeyError, Secim.DoesNotExist):
        # Soruyu oylama biçiminin yeniden görüntünlemesi.
        return render(request, 'anketler/detay.html', {
            'soru': soru,
            'hata_mesaji': "Herhangi bir seçim yapmadınız.",
        })
    else:
        secim_secildi.oylar += 1
        secim_secildi.save()
        '''POST verileri her zaman bir HttpResponseRedirect döndürür.
		Bu, bir kullanıcı "geri" düğmesine basarsa
		verilerin iki kez gönderilmesini önler.'''
        return HttpResponseRedirect(reverse('anketler:sonuclar', args=(soru.id,)))
