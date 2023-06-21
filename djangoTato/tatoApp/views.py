from django.shortcuts import render
from ia.chatbot import tatoBot
# Create your views here.
def home(request):
    return render(request, 'index.html')

def contacto(request):
    detector = tatoBot(model_path='ia/model.h5', tokenizer_path='ia/tokenizer.json', max_seq_length=5)
    is_insult = detector.classify_text(request.POST['content'])
  
    return render(request, 'contacto.html')