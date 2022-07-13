import json
from django.http import HttpResponse
from django.shortcuts import render
from googletrans import Translator


def index(request):
    return render(request, 'index.html')


def transliteration(request):
    msg = request.POST.get('msg')
    translator = Translator()
    data = translator.translate(msg).text
    response = json.dumps(data, default='str')
    return HttpResponse(response)
