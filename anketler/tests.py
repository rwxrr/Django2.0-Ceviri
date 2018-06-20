import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Soru


class SoruModeliTestleri(TestCase):

    def test_yakinda_yayimlanan_gelecektiki_sorular(self):
        """
        yakinda_yayimlanan() yayim_tarihi gelecekte olan sorular için False döndürür.
        """
        zaman = timezone.now() + datetime.timedelta(days=30)
        gelecegin_sorusu = Soru(yayim_tarihi=time)
        self.assertIs(gelecegin_sorusu.yakinda_yayimlanan(), False)
