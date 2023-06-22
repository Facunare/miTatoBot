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
        
        mensaje = Messages.objects.create(content = request.POST['message'])
        print(mensaje)
        oracion = request.POST['message']
        detector = tatoBot(model_path='ia/model.h5', tokenizer_path='ia/tokenizer.json', label_encoder_path='ia/label_encoder.pkl', max_length=13)
        respuesta = detector.responder_oracion(oracion)
        if respuesta:
            answer = Messages.objects.create(content = str(respuesta), response = True)
        print(answer)
       
        return redirect('contacto')
    else:
    
        return render(request, 'contacto.html')
