from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect

from .models import *

menu = [
    {'title': 'О сайте', 'url_name': 'about'},
    {'title': 'Добавить статью', 'url_name': 'add_page'},
    {'title': 'Обратная свзязь', 'url_name': 'contact'},
    {'title': 'Войти', 'url_name': 'login'}
]

def index(request):
    posts = Car.objects.all()
    cats = Category.objects.all()
    context = {
        'posts': posts,
        'cats': cats,
        'menu': menu,
        'title': 'Главная страница',
        'cat_selected': 0
    }
    return render(request, 'cars/index.html', context=context)

def about(request):
    return render(request, 'cars/about.html', {'menu': menu, 'title': "О сайте"})

def addpage(request):
    return HttpResponse("add_page")

def login(request):
    return HttpResponse("login")

def contact(request):
    return HttpResponse("contact")

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')

def show_post(request,post_id):
    return HttpResponse(f"show_post {post_id}")

def show_category(request,cat_id):
    posts = Car.objects.filter(cat_id=cat_id)
    cats = Category.objects.all()

    if len(posts) == 0:
        raise Http404()

    context = {
        'posts': posts,
        'cats': cats,
        'menu': menu,
        'title': 'Отоброжение по рубрикам',
        'cat_selected': cat_id,
    }

    return render(request, 'cars/index.html', context=context)