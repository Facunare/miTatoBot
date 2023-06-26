from django.shortcuts import render, redirect
from ia.chatbot import tatoBot
from .models import Messages, Materias, MateriasConstrucciones, Instalaciones, Proyectos
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

# Create your views here.
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    mensajes = ""
    materias = Materias.objects.all()
    materiasConst = MateriasConstrucciones.objects.all()
    instalaciones = Instalaciones.objects.all()
    proyectos = Proyectos.objects.all()
    
    if request.user.is_authenticated:
        mensajes = Messages.objects.filter(user=request.user)
    
    print(materias)
    
    return render(request, 'index.html', {
        'materias': materias,
        'materiasConst': materiasConst,
        'instalaciones': instalaciones,
        'proyectos': proyectos,
        'mensajes': mensajes
    })

@login_required
def contacto(request):
    mensajes = Messages.objects.all().filter(user = request.user)
    return render(request, 'contacto.html', {
        'mensajes':mensajes
    })
   
@login_required
def ask(request):
    if request.method == 'POST':
        
        mensaje = Messages.objects.create(content = request.POST['message'], user = request.user)
        oracion = request.POST['message']
        detector = tatoBot(model_path='ia/model.h5', tokenizer_path='ia/tokenizer.json', label_encoder_path='ia/label_encoder.pkl', max_length=13)
        respuesta = detector.responder_oracion(oracion)
        if respuesta:
            answer = Messages.objects.create(content = str(respuesta), response = True, user = request.user)
       
        return JsonResponse({'mensaje': request.POST['message'], 'respuesta': respuesta})
    else:
        return render(request, 'contacto.html')
    
@login_required
def deleteChat(request):
    mensajes = Messages.objects.all().filter(user = request.user)
    mensajes.delete()
    request_path = request.GET.get('request_path')
    print(request_path)
    return redirect(request_path)


def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                user.save()
                return redirect('/signin/')
            except:

                return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    'error': 'Usuario existente'
                })
        else:
            return render(request, 'signup.html', {
                'form': UserCreationForm,
                'error': 'Las contraseñas no coinciden'
            })


@login_required
def signout(request):
    logout(request)
    return redirect('/')


def signin(request):
    if request.method == 'GET':

        return render(request, 'signin.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:

            return render(request, 'signin.html', {
                'form': AuthenticationForm,
                'error': "El usuario o contraseña es incorrecto"
            })
        else:
            login(request, user)
            return redirect('/')
