from .views import tolov_usuli,tolov_usuli_grafik,xarajat_update,xarajat_delete,kirim_delete,kirim_update,kirim_detail,xarajat_detail,home_page,xarajat_qoshish,kirim_qoshish,apiratsyalar_page,kalendar_page,kategoriya_grafik
from django.urls import path


urlpatterns=[
    path('',home_page,name="home"),
    path('rashod/',xarajat_qoshish,name='rashod'),
    path('kirim/',kirim_qoshish,name='kirim'),
    path('apiratsya/',apiratsyalar_page,name='apiratsya'),
    path('kalaendar/',kalendar_page,name='kalendar'),
    path('kategorya-grafigi/',kategoriya_grafik,name='kate-graf'),
    path('kirim/<int:pk>/', kirim_detail, name='kirim_detail'),
    path('xarajat/<int:pk>/', xarajat_detail, name='xarajat_detail'),
    path('kirim/<int:pk>/edit/', kirim_update, name='kirim_update'),
    path('kirim/<int:pk>/delete/', kirim_delete, name='kirim_delete'),
    path('xarajat/<int:pk>/delete/',xarajat_delete,name='xarajat_delete'),
    path('xarajat/<int:pk>/edit/',xarajat_update,name="xarajat_update"),
    path('tolov-usuli-grafigi/',tolov_usuli_grafik,name='tolov-graf'),
    path('tolov/',tolov_usuli,name='tolov'),

]