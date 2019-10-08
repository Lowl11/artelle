from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from datetime import datetime, timedelta
from django.contrib.auth.decorators import login_required

import os

from .models import MainInfo
from main.models import Category, Project, ProjectMedia, StudioAudio, StudioImage

################################ MAIN ################################
@login_required(login_url='/cms/login/')
def cms_home_view(request):
    context = {
        'title': 'Главная'
    }
    return render(request, 'cms/index.html', context)

@login_required(login_url='/cms/login/')
def cms_edit_home(request):
    info = MainInfo.objects.get(pk=1)
    context = {
        'title': 'Редактировать страницу "Главная"',
        'info': info
    }
    return render(request, 'cms/edit-home.html', context)

@login_required(login_url='/cms/login/')
def cms_edit_contact(request):
    info = MainInfo.objects.get(pk=1)
    context = {
        'title': 'Редактировать страницу "Контакты"',
        'info': info
    }
    return render(request, 'cms/edit-contact.html', context)

@login_required(login_url='/cms/login/')
def cms_edit_about(request):
    info = MainInfo.objects.get(pk=1)
    if request.method == "POST":
        try:
            about = request.POST['about']
            info.about = about
            info.save()
        except:
            context = {
                'title': 'Редактировать страницу "О Нас"',
                'info': info,
                'error': 'Произошел сбой при сохранении информации'
            }
            return render(request, 'cms/edit-about.html', context)
        context = {
            'title': 'Редактировать страницу "О Нас"',
            'info': info,
            'msg': 'Информация успешно обновлена'
        }
        return render(request, 'cms/edit-about.html', context)


    context = {
        'title': 'Редактировать страницу "О Нас"',
        'info': info
    }
    return render(request, 'cms/edit-about.html', context)

################################ /MAIN ################################





################################ EDIT PAGES ################################
@login_required(login_url='/cms/login/')
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

@login_required(login_url='/cms/login/')
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

@login_required(login_url='/cms/login/')
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
        description = request.POST['description']

        debug(description, 'Description of category with id ' + str(id))

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
            category1.description = description
            if img:
                path = category1.image.path
                os.remove(path)
                category1.image = image
            category1.save()
        elif id == 2:
            category2.name = title
            category2.description = description
            if img:
                path = category2.image.path
                os.remove(path)
                category2.image = image
            category2.save()
        elif id == 3:
            category3.name = title
            category3.description = description
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

@login_required(login_url='/cms/login/')
def cms_projects(request):
    projects = Project.objects.all()
    for p in projects:
        cat_id = p.category_id
        p.category_name = Category.objects.get(pk=cat_id).name
    context = {
        'title': 'Проекты',
        'projects': reversed(projects)
    }
    return render(request, 'cms/projects.html', context)

@login_required(login_url='/cms/login/')
def cms_projects_new(request):
    if request.method == "POST":
        name = request.POST['name']
        description = request.POST['description']
        date = request.POST['date']
        cat = request.POST['category']

        # YYYY-MM-DD
        # 02-08-2019 0-1-2
        darr = date.split('/')
        date = darr[2] + '-' + darr[1] + '-' + darr[0]

        category = Category.objects.get(name=cat)

        if name == '' or description == '' or date == '' or category is None:
            context = {
                'title': 'Новый проект',
                'error': 'Один или несколько полей не были заполнены'
            }
            return render(request, 'cms/new-project.html', context)

        project = Project()
        project.category_id = category.id
        project.name = name
        project.description = description
        project.date = date
        project.save()

        return redirect('/cms/projects/')

    categories = Category.objects.all()
    context = {
        'title': 'Новый проект',
        'categories': categories
    }
    return render(request, 'cms/new-project.html', context)

@login_required(login_url='/cms/login/')
def cms_project(request):
    if request.method == "POST":
        id = request.POST['id']
        name = request.POST['name']
        description = request.POST['description']
        date = request.POST['date']
        cat = request.POST['category']

        darr = date.split('/')
        date = darr[2] + '-' + darr[1] + '-' + darr[0]

        category = Category.objects.get(name=cat)

        project = Project.objects.get(pk=id)
        project.category_id = category.id
        project.name = name
        project.description = description
        project.date = date
        project.save()

        return redirect('/cms/projects/project/?id=' + str(id))

    try:
        id = request.GET['id']
        project = Project.objects.get(pk=id)
        formatted = str(project.date).split('-')
        project.formatted = formatted[2] + '/' + formatted[1] + '/' + formatted[0]
        images = ProjectMedia.objects.filter(project=project, type=1)
        videos = ProjectMedia.objects.filter(project=project, type=2)
    except:
        return redirect('/cms/projects/')
    
    categories = Category.objects.all()

    context = {
        'title': 'Редактировать проект',
        'project': project,
        'images': images,
        'videos': videos,
        'categories': categories
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
    
    if request.method == "GET":
        if request.GET['action'] == 'delete':
            try:
                delete_id = request.GET['id']
                project = Project.objects.get(pk=delete_id)
                media = ProjectMedia.objects.filter(project=project)
                if media is not None:
                    for m in media:
                        path = media.image.path
                        os.remove(path)
                        m.delete()
                project.delete()
                return HttpResponse('1')
            except:
                debug('Issue with try/catch delete project', 'Exception')
                return HttpResponse('0')
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





################################ STUDIO ################################
def cms_studio_audio(request):
    if request.method == "POST":
        action = request.POST['action']
        if action == 'edit':
            id = request.POST['id']
            name = request.POST['name']
            audio = StudioAudio.objects.get(pk=id)

            try:
                file = request.FILES['audio']
                path = audio.audio.path
                os.remove(path)

                ext = get_extension(file.name)
                file.name = 'audio-' + str(audio.id) + '.' + ext
                audio.audio = file
            except:
                pass

            audio.name = name
            audio.save()
        elif action == 'add':
            name = request.POST['name']
            file = request.FILES['audio']

            audio = StudioAudio()
            audio.name = name
            audio.save()

            ext = get_extension(file.name)
            file.name = 'audio-' + str(audio.id) + '.' + ext

            audio.audio = file
            audio.save()
        return redirect('/cms/studio/audio/')

    audios = StudioAudio.objects.all()
    context = {
        'title': 'Ауидо записи - Студия',
        'audios': reversed(audios)
    }
    return render(request, 'cms/audios.html', context)

def cms_studio_audio_get(request):
    try:
        id = request.GET['id']
        action = request.GET['action']
        if action == 'delete':
            audio = StudioAudio.objects.get(pk=id)
            audio.delete()
            return HttpResponse('1')
        return HttpResponse('-1')
    except:
        pass
    return HttpResponse('0')

def cms_studio_images(request):
    if request.method == 'POST':
        image = request.FILES['image']
        info = MainInfo.objects.get(pk=1)

        id = info.si_counter + 1
        ext = get_extension(image.name)
        image.name = 'image-' + str(id) + '.' + ext

        info.si_counter = id
        info.save()

        si = StudioImage()
        si.image = image
        si.save()

        return redirect('/cms/studio/images/')
    images = StudioImage.objects.all()
    context = {
        'title': 'Изображения - Студия',
        'images': images
    }
    return render(request, 'cms/images.html', context)

def cms_si_delete(request):
    if request.method == "GET":
        try:
            id = request.GET['id']
            si = StudioImage.objects.get(pk=id)
            path = si.image.path
            os.remove(path)
            si.delete()
            return HttpResponse('1')
        except:
            pass
    return HttpResponse('0')

################################ /STUDIO ################################





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
    dot_counter = 0
    for i in range(0, len(file)):
        if file[i] == '.':
            dot_counter += 1
    
    tmp_dot_counter = 0
    result = ''
    dot = False
    for i in range(0, len(file)):
        if dot:
            result += file[i]
        if file[i] == '.' and dot == False:
            tmp_dot_counter += 1
            if tmp_dot_counter == dot_counter:
                dot = True
    return result

def type(file):
    ext = get_extension(file.name)
    if ext == 'mp4':
        return 2
    return 1
