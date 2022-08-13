from django.shortcuts import render
from googletrans import Translator

# Create your views here.

def translate_text(request):
    if request.method == "POST":
        lang = request.POST.get("lang", None)
        txt = request.POST.get("txt", None)

        translator = Translator()
        translation = translator.translate(txt, dest=lang)

        return render(request, 'translate.html', {"result": translation.text})

    return render(request, 'translate.html')