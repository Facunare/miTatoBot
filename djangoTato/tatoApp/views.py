from django.shortcuts import render
from ia.chatbot import tatoBot
# Create your views here.
def home(request):
    return render(request, 'index.html')

def contacto(request):
    return render(request, 'contacto.html')

def ask(request):
    if request.method == 'POST':
        oracion = request.POST['message']
        print(oracion)
        detector = tatoBot(model_path='ia/model.h5', tokenizer_path='ia/tokenizer.json', max_length=13)

        # Etiquetas de entrenamiento
        etiquetas = ['¡Hola! me llamo Tatobot', '¡Hola! Estoy muy bien ¿y tu?', 'La escuela se llama Almirante Guillermo Brown mejor conocida como ET36', 'El colegio queda en el Polo educativo Saavedra en la calle Galvan 3700', 'El colegio se llama Almirante Guillermo Brown', 'El nombre abreviado del colegio es ET36', 'El colegio se encuentra en el barrio de Saavedra']
        # Ajustar el LabelEncoder con los datos de entrenamiento
        detector.label_encoder.fit(etiquetas)

        respuesta = detector.responder_oracion(oracion)
        print(respuesta)
        return render(request, 'contacto.html', {'respuesta': respuesta})
    else:
        return render(request, 'contacto.html')
