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
        detector = tatoBot(model_path='ia/model.h5', tokenizer_path='ia/tokenizer.json', max_seq_length=13)
        respuesta = detector.response(oracion)
        return render(request, 'contacto.html', {'respuesta': respuesta})
    else:
        return render(request, 'contacto.html')
