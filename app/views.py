from django.http import HttpResponse
from django.shortcuts import render, reverse
import datetime
import os


def home_view(request):
    template_name = 'app/home.html'
    # впишите правильные адреса страниц, используя
    # функцию `reverse`
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }
    
    # context и параметры render менять не нужно
    # подбробнее о них мы поговорим на следующих лекциях
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    # обратите внимание – здесь HTML шаблона нет, 
    # возвращается просто текст
    current_time = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    msg = f'Текущее время: {current_time}'
    return HttpResponse(msg)


def workdir_view(request):
    str_temp = ''
    for i in range(len(os.listdir('.'))):
        dir_app = os.listdir('.')[i]
        str_temp = str_temp + (f'{dir_app}\t'+'<br>')
    return HttpResponse(str_temp)
