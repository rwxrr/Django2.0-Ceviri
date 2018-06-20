import datetime
from django.db import models
from django.utils import timezone


class Soru(models.Model):
    soru_metni = models.CharField(max_length=200)
    yayim_tarihi = models.DateTimeField('yayımlanma tarihi')

    def __str__(self):
        return self.soru_metni

    def yakinda_yayimlanan(self):
        suanki_zaman = timezone.now()
        return suanki_zaman - datetime.timedelta(days=1) <= self.yayim_tarihi <= suanki_zaman
        yakin_zamanda_yayinlanan.admin_order_field = 'yayim_tarihi'
        yakin_zamanda_yayinlanan.boolean = True
        yakin_zamanda_yayinlanan.short_description = 'Yakında yayımlanan?'


class Secim(models.Model):
    soru = models.ForeignKey(Soru, on_delete=models.CASCADE)
    secim_metni = models.CharField(max_length=200)
    oylar = models.IntegerField(default=0)

    def __str__(self):
        return self.secim_metni
