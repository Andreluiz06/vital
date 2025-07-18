from django.shortcuts import redirect, render
from django.contrib.messages import constants
from django.contrib import messages 
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate

#Função cadastro

def cadastro(request):
    if request.user.is_authenticated:
        return redirect('home')
        
    if request.method == "GET":
        return render(request, 'cadastro.html')
    else:
        primeiro_nome = request.POST.get('primeiro_nome')
        ultimo_nome = request.POST.get('ultimo_nome')
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')

        if not senha == confirmar_senha:    
            messages.add_message(request, constants.ERROR, 'Cadastre uma senha forte')
            return redirect('cadastro')

        
        if len(senha) < 6:
            messages.add_message(request, constants.ERROR, 'As senhas não coincidem')
            return redirect('cadastro')
        
        try:
            # Username deve ser único!
            User.objects.create_user(
                first_name=primeiro_nome,
                last_name=ultimo_nome,
                username=username,
                email=email,
                password=senha,
            )
        except:
            
            messages.add_message(request, constants.ERROR, 'Senha não coincide realize novamente')
            return redirect('cadastro')
        
        messages.add_message(request, constants.SUCCESS, 'Seu Cadastro foi realizado com sucesso!!!')
        return redirect('login')
    

#view logar

def logar(request):
    if request.user.is_authenticated:
        return redirect('home')
        
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        user = authenticate(username=username, password=senha)

        if user:
            login(request, user)
						# Acontecerá um erro ao redirecionar por enquanto, resolveremos nos próximos passos
            return redirect('/')
        else:
            messages.add_message(request, constants.ERROR, 'Usuario ou senha inválidos')
            return redirect('login')
        
#view Home

def home(request):
    # Se o usuário estiver autenticado, passamos o nome dele para o template
    if request.user.is_authenticated:
        nome = request.user.first_name
        return render(request, 'home.html', {'nome': nome})
    
    return render(request, 'home.html')

#Sair
def sair(request):
    logout(request)
    return redirect('/')