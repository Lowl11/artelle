from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from datetime import datetime, timedelta
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from .viewmodel import MainViewModel
from .dbcontext import MainDbContext
from .debugger import Debugger

############## Actions ##############

def home_view(request):
    vm = MainViewModel('Главная страница', 'start', MainDbContext.GetMainInfo())
    return vm.Render(request, 'main/index.html')

def send_email(request):
    if request.method == "POST":
        title = 'Hello from Lazy Owl'
        text = render_to_string('main/mail.html')
        text = strip_tags(text)
        sender = 'slimsly11@gmail.com'
        receivers = ['mm.slimshady@yandex.kz']

        send_mail(title, text, sender, receivers, fail_silently=True)
        return redirect('/studio/')
    return HttpResponse('0')

def about_view(request):
    vm = MainViewModel('О Нас', 'about', MainDbContext.GetMainInfo())
    vm.Settings(simple_page = True, responsive_height = True)
    return vm.Render(request, 'main/about.html')

def projects_view(request):
    vm = MainViewModel('Категории проектов', 'projects')
    vm.Settings(simple_page = True, responsive_height = True)
    vm.AddObject('categories', MainDbContext.GetCategories())
    return vm.Render(request, 'main/categories.html')

def studio_view(request):
    vm = MainViewModel('Студия', 'studio')
    vm.Settings(responsive_height = False)
    vm.AddObject('audios', MainDbContext.GetStudioAudios())
    vm.AddObject('images', MainDbContext.GetStudioImages())
    return vm.Render(request, 'main/studio.html')

def contact_view(request):
    vm = MainViewModel('Контакты', 'contact', MainDbContext.GetMainInfo())
    vm.Settings(responsive_height = False)
    return vm.Render(request, 'main/contact.html')

def projects_list_view(request):
    try:
        _id = request.GET['id']
    except:
        return redirect('/categories/')

    vm = MainViewModel('Проекты', 'projects')
    vm.Settings(True, True)
    vm = MainDbContext.GetProjects(_id, vm)
    if type(vm) is MainViewModel:
        return vm.Render(request, 'main/projects.html')
    
    return redirect('/categories/')
