from django.db import models


class MainInfo(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок домашней страницы')
    subtitle1 = models.CharField(max_length=100, verbose_name='Подзаголовок домашней страницы №1', default='')
    subtitle2 = models.CharField(max_length=100, verbose_name='Подзаголовок домашней страницы №2', default='')
    subtitle3 = models.CharField(max_length=100, verbose_name='Подзаголовок домашней страницы №3', default='')
    address = models.CharField(max_length=100, default='', verbose_name='Адрес компании')
    phone1 = models.CharField(max_length=20, default='', verbose_name='Номер телефона №1')
    phone2 = models.CharField(max_length=20, default='', verbose_name='Номер телефона №2')
    phone3 = models.CharField(max_length=20, default='', verbose_name='Номер телефона №3')
    mail = models.CharField(max_length=100, default='', verbose_name='Почтовый ящик компании')
    video = models.FileField(upload_to='home/', verbose_name='Видео Главной Страницы', null=True)
    about = models.TextField(verbose_name='Текст на странице о нас', default='')
    si_counter = models.IntegerField(default=0, verbose_name='Счетчик изображений студии')

    def __str__(self):
        return 'Основная информация о сайте'

    class Meta:
        verbose_name_plural = "Информация о сайте"
    
