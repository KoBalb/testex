from django.shortcuts import render
from django.http import HttpResponse
from .models import UserText

def index(request):
    if request.method == "POST":
        text = request.POST.get("text")  # Получаем данные из формы
        if text:  # Если текст не пустой
            # Сохраняем текст в базе данных
            UserText.objects.create(text=text)
        return HttpResponse(f"Текст сохранён: {text}")  # Отправляем ответ

    # Получаем все сохранённые тексты
    texts = UserText.objects.all()
    return render(request, "main/index.html", {"texts": texts})