from django.shortcuts import render, redirect

class MainViewModel:
    __context = {}

    def __init__(self, title, page_id, info = None):
        self.__context['title'] = title
        self.__context['page_id'] = page_id
        if info != None:
            self.__context['info'] = info

    def Render(self, request, path):
        return render(request, path, self.__context)

    def AddObject(self, object_name, object):
        self.__context[object_name] = object

    def Settings(self, simple_page = True, responsive_height = True):
        self.__context['simple'] = 'simple-page' if simple_page else ''
        self.__context['simple'] += ' responsive-height' if responsive_height else ''

    def GetContext(self):
        return self.__context

    def __str__(self):
        return 'MainViewModal:\n' + str(self.__context)
