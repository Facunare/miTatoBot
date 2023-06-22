from django.shortcuts import render, redirect
from ia.chatbot import tatoBot
from .models import Messages
# Create your views here.
def home(request):
    return render(request, 'index.html')

def contacto(request):
    mensajes = Messages.objects.all()
    return render(request, 'contacto.html', {
        'mensajes':mensajes
    })
   

def ask(request):
    if request.method == 'POST':
        
        Messages.objects.create(content = request.POST['message'])
        
        oracion = request.POST['message']
        detector = tatoBot(model_path='ia/model.h5', tokenizer_path='ia/tokenizer.json', max_length=13)
        respuesta = detector.responder_oracion(oracion)
        if respuesta:
            Messages.objects.create(content = str(respuesta), response = True)

        return redirect('contacto')
    else:
    
        return render(request, 'contacto.html')
