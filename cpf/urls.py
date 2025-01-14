from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"), #path vazio para informar se o sistema está rodando
    path("<str:value>", views.checa_cpf, name="checa_cpf"), #path dinâmico para informar o cpf na url
]