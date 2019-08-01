from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from datetime import datetime, timedelta

from .models import Category, Project, ProjectMedia
from cms.models import MainInfo

def home_view(request):
    info = MainInfo.objects.get(pk=1)
    context = {
        'title': 'Главная страница',
        'page_id': 'start',
        'info': info
    }
    return render(request, 'main/index.html', context)

def about_view(request):
    context = {
        'title': 'О Нас',
        'page_id': 'about',
        'simple': 'simple-page responsive-height'
    }
    return render(request, 'main/about.html', context)

def projects_view(request):
    categories = Category.objects.all()
    context = {
        'title': 'Категории проектов',
        'page_id': 'projects',
        'simple': 'simple-page',
        'categories': categories
    }
    return render(request, 'main/categories.html', context)

def studio_view(request):
    context = {
        'title': 'Студия',
        'page_id': 'studio',
        'simple': 'simple-page'
    }
    return render(request, 'main/studio.html', context)

def contact_view(request):
    info = MainInfo.objects.get(pk=1)
    context = {
        'title': 'Контакты',
        'page_id': 'contact',
        'simple': 'simple-page',
        'info': info
    }
    return render(request, 'main/contact.html', context)

def projects_list_view(request):
    try:
        id = request.GET['id']
        projects = Project.objects.filter(category_id=id)

        for p in projects:
            images = ProjectMedia.objects.filter(project=p)
            p.image = images[0].image
    except:
        return redirect('/categories/')

    images = ProjectMedia.objects.all()
    array = []
    for p in Project.objects.all():
        p_arr = images.filter(project=p)
        array.append(p_arr)

    context = {
        'title': 'Проекты',
        'projects': projects,
        'page_id': 'projects',
        'simple': 'simple-page responsive-height',
        'images': array
    }
    return render(request, 'main/projects.html', context)

def debug(msg, pre = '0'):
    print('\n--------------------------------------------–')
    if pre != '0':
        print(pre + ':')
    print(msg)
    print('--------------------------------------------–\n')
