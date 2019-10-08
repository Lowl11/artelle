from .models import Category, Project, ProjectMedia, StudioAudio, StudioImage
from cms.models import MainInfo
from .viewmodel import MainViewModel

from .debugger import Debugger

class MainDbContext:

    @staticmethod
    def GetMainInfo():
        info = MainInfo.objects.get(pk=1)
        return info
    
    @staticmethod
    def GetCategories():
        return Category.objects.all()

    @staticmethod
    def GetStudioAudios():
        return StudioAudio.objects.all()
    
    @staticmethod
    def GetStudioImages():
        return StudioImage.objects.all()

    @staticmethod
    def GetProjects(id, vm):
        try:
            projects = Project.objects.filter(category_id=id)
            category = Category.objects.get(pk=id)

            for p in projects:
                images = ProjectMedia.objects.filter(project=p)
                p.image = images[0].image
        except:
            return False

        images = ProjectMedia.objects.all()
        array = []
        for p in Project.objects.all():
            p_arr = images.filter(project=p)
            array.append(p_arr)
        
        vm.AddObject('projects', projects)
        vm.AddObject('images', array)
        vm.AddObject('category', category)
        return vm

    def __str__(self):
        return 'Main Database Context'
    
