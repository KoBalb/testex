from django.shortcuts import render
from .models import Text
from django.http import HttpResponse
# Create your views here.
def index(request):
    text = Text.objects.all()
    return render(request, 'main/index.html', {"text": text})
