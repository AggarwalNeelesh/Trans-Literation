import json
from django.http import HttpResponse
from django.shortcuts import render
from googletrans import Translator


def index(request):
    # Method to telecast the main page

    return render(request, 'index.html')


def transliteration(request):
    # Method for translating any language into English

    msg = request.POST.get('msg')
    translator = Translator()
    data = translator.translate(msg).text
    response = json.dumps(data, default='str')

    return HttpResponse(response)
