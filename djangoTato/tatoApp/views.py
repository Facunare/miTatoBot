from django.shortcuts import render
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
        
        # oracion = request.POST['message']
        # detector = tatoBot(model_path='ia/model.h5', tokenizer_path='ia/tokenizer.json', max_length=13)
        # etiquetas = ['¡Hola! me llamo Tatobot', '¡Hola! Estoy muy bien ¿y tu?', 'La escuela se llama Almirante Guillermo Brown mejor conocida como ET36', 'El colegio queda en el Polo educativo Saavedra en la calle Galvan 3700', 'El colegio se llama Almirante Guillermo Brown', 'El nombre abreviado del colegio es ET36', 'El colegio se encuentra en el barrio de Saavedra']
        # detector.label_encoder.fit(etiquetas)
        # respuesta = detector.responder_oracion(oracion)
        # return render(request, 'contacto.html', {'respuesta': respuesta})
        return render(request, 'contacto.html')
    else:
    
        return render(request, 'contacto.html')
