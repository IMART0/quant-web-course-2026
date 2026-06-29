from unittest import result

from django.shortcuts import render

# Create your views here.



from django.http import HttpResponse

def main_page(request):
    return HttpResponse('Добро пожаловать на офицальны сайт лагеря Квант!')


def courses(request):
    result = ""