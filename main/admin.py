from django.contrib import admin

from .models import Category, Project, ProjectMedia, StudioAudio, StudioImage

# Register your models here.
admin.site.register(Category)
admin.site.register(Project)
admin.site.register(ProjectMedia)
admin.site.register(StudioAudio)
admin.site.register(StudioImage)