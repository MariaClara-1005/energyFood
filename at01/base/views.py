from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def erro(request):
    return render(request, 'base/telaTest.html')

@login_required
def pagamento(request):
    return render(request, 'base/pagamento.html')

@login_required
def opcoes(request):
    return render(request, 'base/eteHome.html')

@login_required
def carrinho(request):
    return render(request, 'base/carrinho2.html')

@login_required
def escolha(request):
    return render(request, 'base/escolha.html')

def inicio(request):
    return render(request, 'base/inicio2.html')

def sair(request):
    logout(request)
    return redirect(home)

def home(request):
    if request.method == "POST":
        usuario = request.POST.get('user_cad')
        senha = request.POST.get('senha_cad')

        # Autentica o usuário
        usu = authenticate(username=usuario, password=senha)

        if usu is not None:
            # Login do usuário
            login(request, usu)

            return redirect('opcoes') 
        else:
            return render(request, 'base/login.html', {'msg': "Dados incorretos!"})

    return render(request, 'base/login.html', {'msg': ''})

def cadastro(request):
    #Cadastro.objects.all().delete()
    if request.method == "POST":
        usuario = request.POST.get('user_cad')
        nome_completo = request.POST.get('nome_cad')
        email = request.POST.get('email_cad')
        contato = request.POST.get('number_cad')
        senha = request.POST.get('senha_cad')

        # Verifica se o usuário já existe
        if User.objects.filter(username=usuario).exists():
            return render(request, 'base/cadastro.html', {'msg': "Usuário já existe. Tente outro."})

        # Cria um novo superusuário
        User.objects.create_user(username=usuario, email=email, password=senha)

        #salvar infor no banco
        Cadastro(usuario=usuario, email=email, contato=contato, nome_completo=nome_completo, senha=senha).save()

        return redirect('home')  # Redireciona para a página de login após o cadastro

    return render(request, 'base/cadastro.html', {'msg': ''})



