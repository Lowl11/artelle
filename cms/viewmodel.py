from django.shortcuts import render, redirect

class CmsViewModel:
    __context = {}

    def __init__(self, title, info = None):
        self.__context['title'] = title
        if info != None:
            self.__context['info'] = info

    def Render(self, request, path):
        return render(request, path, self.__context)

    def AddObject(self, object_name, object):
        self.__context[object_name] = object

    def GetContext(self):
        return self.__context

    def __str__(self):
        return 'CmsViewModal:\n' + str(self.__context)
