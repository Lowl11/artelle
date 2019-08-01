from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from datetime import datetime, timedelta
from django.contrib.auth.decorators import login_required

import os

from .models import MainInfo
from main.models import Category, Project, ProjectMedia

################################ MAIN ################################
@login_required
def cms_home_view(request):
    context = {
        'title': 'Главная'
    }
    return render(request, 'cms/index.html', context)

@login_required
def cms_edit_home(request):
    info = MainInfo.objects.get(pk=1)
    context = {
        'title': 'Редактировать страницу "Главная"',
        'info': info
    }
    return render(request, 'cms/edit-home.html', context)

@login_required
def cms_edit_contact(request):
    info = MainInfo.objects.get(pk=1)
    context = {
        'title': 'Редактировать страницу "Контакты"',
        'info': info
    }
    return render(request, 'cms/edit-contact.html', context)

@login_required
def cms_edit_about(request):
    info = MainInfo.objects.get(pk=1)
    context = {
        'title': 'Редактировать страницу "О Нас"',
        'info': info
    }
    return render(request, 'cms/edit-about.html', context)

################################ /MAIN ################################





################################ EDIT PAGES ################################
def cms_edit_main(request):
    if request.method == "POST":
        title = request.POST['title']
        subtitle1 = request.POST['subtitle1']
        subtitle2 = request.POST['subtitle2']
        subtitle3 = request.POST['subtitle3']

        info = MainInfo.objects.get(pk=1)
        info.title = title
        info.subtitle1 = subtitle1
        info.subtitle2 = subtitle2
        info.subtitle3 = subtitle3
        info.save()

        context = {
            'title': 'Редактировать страницу "Главная"',
            'info': info,
            'msg': 'Информация была успешно обновлена'
        }
        return render(request, 'cms/edit-home.html', context)
    return redirect('/cms/edithome/')

def cms_edit_main_upload(request):
    if request.method == "POST":
        video = request.FILES['file']
        info = MainInfo.objects.get(pk=1)

        path = info.video.url
        
        files = []
        # r=root, d=directories, f = files
        for r, d, f in os.walk('/media/projects/'):
            for file in f:
                files.append(os.path.join(r, file))

        debug('Cycle size: ' + str(len(files)), 'Pre cycle message')
        for f in files:
            debug(f)

        os.remove(path)

        video.name = 'promo.mp4'
        info.video = video
        info.save()

        context = {
            'title': 'Редактировать страницу "Главная"',
            'info': info,
            'video_msg': 'Видео было успешно обновлено'
        }
        return render(request, 'cms/edit-home.html', context)
    return redirect('/cms/edithome/')

def cms_edit_contact_post(request):
    if request.method == "POST":
        address = request.POST['address']
        phone1 = request.POST['phone1']
        phone2 = request.POST['phone2']
        phone3 = request.POST['phone3']
        mail = request.POST['mail']

        info = MainInfo.objects.get(pk=1)
        info.address = address
        info.phone1 = phone1
        info.phone2 = phone2
        info.phone3 = phone3
        info.mail = mail
        info.save()

        context = {
            'title': 'Редактировать страницу "Контакты"',
            'info': info,
            'msg': 'Информация была успешно обновлена'
        }
        return render(request, 'cms/edit-contact.html', context)
    return redirect('/cms/editcontact/')

################################ /EDIT PAGES ################################




################################ CATEGORIES ################################
@login_required(login_url='/cms/login/')
def cms_categories(request):
    post = False
    if request.method == "POST":
        id = int(request.POST['id'])
        title = request.POST['title']
        img = False
        try:
            image = request.FILES['image']
            ext = get_extension(image.name)
            image.name = 'category-' + str(id) + '.' + ext
            img = True
        except:
            img = False

        category1 = Category.objects.get(pk=1)
        category2 = Category.objects.get(pk=2)
        category3 = Category.objects.get(pk=3)
        
        if id == 1:
            category1.name = title
            if img:
                path = category1.image.path
                os.remove(path)
                category1.image = image
            category1.save()
        elif id == 2:
            category2.name = title
            if img:
                path = category2.image.path
                os.remove(path)
                category2.image = image
            category2.save()
        elif id == 3:
            category3.name = title
            if img:
                path = category3.image.path
                os.remove(path)
                category3.image = image
            category3.save()
        post = True
            

    if not post:
        category1 = Category.objects.get(pk=1)
        category2 = Category.objects.get(pk=2)
        category3 = Category.objects.get(pk=3)

    context = {
        'title': 'Категории',
        'category1': category1,
        'category2': category2,
        'category3': category3
    }

    if post:
        text = 'Данные успешно изменены'
        if id == 1:
            context['msg1'] = text
        elif id == 2:
            context['msg2'] = text
        elif id == 3:
            context['msg3'] = text
    return render(request, 'cms/categories.html', context)

def cms_projects(request):
    projects = Project.objects.all()
    context = {
        'title': 'Проекты',
        'projects': reversed(projects)
    }
    return render(request, 'cms/projects.html', context)

def cms_projects_new(request):
    if request.method == "POST":
        name = request.POST['name']
        description = request.POST['description']

        project = Project()
        project.name = name
        project.description = description
        project.date = datetime.now()
        project.save()

        return redirect('/cms/projects/')

    context = {
        'title': 'Новый проект'
    }
    return render(request, 'cms/new-project.html', context)

@login_required(login_url='/cms/login/')
def cms_project(request):
    if request.method == "POST":
        id = request.POST['id']
        name = request.POST['name']
        description = request.POST['description']
        # здесь datetime должен быть

        project = Project.objects.get(pk=id)
        project.name = name
        project.description = description
        # здесь datetime должен быть
        project.save()

        return redirect('/cms/projects/project/?id=' + str(id))

    try:
        id = request.GET['id']
        project = Project.objects.get(pk=id)
        images = ProjectMedia.objects.filter(project=project, type=1)
        videos = ProjectMedia.objects.filter(project=project, type=2)
    except:
        return redirect('/cms/projects/')
    
    context = {
        'title': 'Редактировать проект',
        'project': project,
        'images': images,
        'videos': videos
    }
    return render(request, 'cms/edit-project.html', context)

def cms_project_upload(request):
    if request.method == "POST":
        id = request.POST['id']
        file = request.FILES['file']

        project = Project.objects.get(pk=id)
        last_media = project.last_media + 1
        project.last_media = last_media
        project.save()

        ext = get_extension(file.name)
        file.name = 'project-' + str(id) + '-' + str(last_media) + '.' + ext

        media = ProjectMedia()
        media.project = project
        if type(file) == 1:
            media.image = file
            media.type = 1
        else:
            media.video = file
            media.type = 2
        media.save()

        return redirect('/cms/projects/project/?id=' + str(id))
    return redirect('/cms/projects/')

def cms_project_delete(request):
    if request.method == "GET":
        try:
            id = request.GET['id']
            image = ProjectMedia.objects.get(pk=id)
            path = image.image.path
            os.remove(path)
            image.delete()
            return HttpResponse('1')
        except:
            pass
    return HttpResponse('0')

################################ /CATEGORIES ################################





################################ AUTH ################################
def login_vp(request):
    error = False
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/cms/')
        error = True
    
    context = {
        'title': 'Авторизация'
    }
    if error:
        context['error'] = 'Неверное имя пользователя или пароль'
    return render(request, 'cms/login.html', context)

def logout_g(request):
    logout(request)
    return redirect('/cms/login/')

################################ /AUTH ################################





def debug(msg, pre = '0'):
    print('\n--------------------------------------------–')
    if pre != '0':
        print(pre + ':')
    print(msg)
    print('--------------------------------------------–\n')

def get_extension(file):
    dot = False
    result = ''
    for i in range(0, len(file)):
        if dot:
            result += file[i]

        if file[i] == '.':
            dot = True
    
    return result

def type(file):
    ext = get_extension(file.name)
    if ext == 'mp4':
        return 2
    return 1
