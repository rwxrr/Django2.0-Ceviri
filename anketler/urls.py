from django.urls import path

from . import views

app_name = 'anketler'

urlpatterns = [
    path('', views.AnasayfaView.as_view(), name='anasayfa'),
    path('<int:pk>/', views.DetayView.as_view(), name='detay'),
    path('<int:pk>/sonuclar/', views.SonuclarView.as_view(), name='sonuclar'),
    path('<int:soru_id>/oy/', views.oy, name='oy'),
]
