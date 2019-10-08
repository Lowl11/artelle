from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=300)
    image = models.ImageField(upload_to='category/', verbose_name='Изображение категории')
    description = models.TextField(verbose_name='Описание категории', default='')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Категории"
    
    

class Project(models.Model):
    category_id = models.IntegerField(default=0)
    name = models.CharField(max_length=200, verbose_name='Название проекта')
    description = models.TextField(verbose_name='Описание проекта')
    date = models.DateField(verbose_name='Дата проекта')
    last_media = models.IntegerField(default=0, verbose_name='ID последнего файла')

    def __str__(self):
        return self.name + ' (' + str(self.date) + ')'

    class Meta:
        verbose_name_plural = "Проекты"
    
    

class ProjectMedia(models.Model):
    project = models.ForeignKey(Project, default=None, on_delete=models.CASCADE, verbose_name='Проект')
    image = models.ImageField(upload_to='projects/', verbose_name='Изображение', blank=True)
    video = models.FileField(upload_to='projects/', verbose_name='Видео', blank=True)
    type = models.IntegerField(default=0)

    def __str__(self):
        return 'Медиа файл проекта "' + self.project.name + '" [ID: ' + str(self.id) + ']'

    class Meta:
        verbose_name_plural = "Медиа файлы Проектов"


class StudioAudio(models.Model):
    name = models.CharField(max_length=300)
    audio = models.FileField(upload_to='studio_sounds/', verbose_name='Аудио запись', null=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Аудиозаписи Студии"


class StudioImage(models.Model):
    image = models.ImageField(upload_to='studio_images/', verbose_name='Изображение')

    def __str__(self):
        return 'Изображение студии #' + str(self.id)

    class Meta:
        verbose_name_plural = "Изображения Студии"

