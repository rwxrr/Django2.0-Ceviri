from django.contrib import admin

from .models import Secim, Soru


class SecimInline(admin.TabularInline):
    model = Secim
    extra = 3


class SoruAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['soru_metni']}),
        ('Tarih Bilgisi', {'fields': ['yayim_tarihi'], 'classes': ['collapse']}),
    ]
    inlines = [SecimInline]
    list_display = ('soru_metni', 'yayim_tarihi', 'yakinda_yayimlanan')
    list_filter = ['yayim_tarihi']
    search_fields = ['soru_metni']


admin.site.register(Soru, SoruAdmin)
