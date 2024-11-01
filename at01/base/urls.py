from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path('', views.home, name='home'),
    path('erro', views.erro, name='erro'),
    path('pagamento', views.pagamento, name='pagamento'),
    path('opcoes', views.opcoes, name='opcoes'),
    path('carrinho', views.carrinho, name='carrinho'),
    path('escolha', views.escolha, name='escolha'),
    path('inicio', views.inicio, name='inicio'),
    path('cadastro', views.cadastro, name='cadastro'),
    path('sair', views.sair, name='sair'),
] 