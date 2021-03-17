from django.db.models import \
    (Model, ImageField, DateTimeField, ForeignKey, IntegerField, CASCADE, DO_NOTHING)
from django.db import models
from media_service.settings import AUTH_USER_MODEL
from django.conf import settings

User = settings.AUTH_USER_MODEL




class ImageStorage(Model):

    user = ForeignKey(User, on_delete=CASCADE, related_name='images_created')
    image = ImageField(upload_to='images/%Y/%m/%d', blank=True, verbose_name='Изображение')
    timestamp = DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name = 'Хранилище изоборажений'
        verbose_name_plural = 'Хранилище изоборажений'


    def __str__(self):
        output = str(self.image).split('/')[-1]
        return output

    def __repr__(self):
        output = str(self.image).split('/')[-1]
        return output



class History(Model):

    CAUSE_CHOICES = (
        (1, 'Изображение создано'),
        (2, 'Изображение изменено'),
        (3, 'Изображение удалено'),
    )

    image = ForeignKey(ImageStorage, on_delete=DO_NOTHING, related_name='history')
    cause = IntegerField(choices=CAUSE_CHOICES)# get_cause_display()
    timestamp = DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name = 'История изменений'
        verbose_name_plural = 'История изменений'


    def __str__(self):
        return str(self.timestamp)


"""Валидацию размера изображения можно попытаться сделать в формах clean_ , или в валидаторах"""


"""
ЗАДАНИЕ
Создать одностраничный сайт на Django 3
СО страницы можно отправить картинку на сервер в папку 'media' асинхронно (без перезагрузки).
Максимальный размер файла ограничивается django и составляет 2 Mb. 
Отправить может только зарегистрированный пользователь (зарегистрироваться должен самостоятельно). 
После загрузки файла в базу данных (любая совместимая СУБД) в таблицу записывается 
3 отдельных поля: логин пользователя, дата-время записи и путь к загруженному файлу.
После записи в базу на эл. почту пользователя отправляется 
письмо со значениями всех трех полей в теле через точку с запятой.
У пользователя должен быть личный кабинет, в котором можно перезагрузить любую из загруженных им картинок.
Должна быть возможность посмотреть историю изменений каждого изображения
"""

# 1 создать личный кабинет
# 2 вывести все сохраненные изображения пользователя
# 3 вывести историю изменений этих изображения
# 4 сделать чтобы их можно было менять прямо от туда
# 5 сделать валидатор загрузки изображения в 2 мб
# 6 сделать чтобы при загрузке изображения посылалось письмо

"""СО страницы можно отправить картинку на сервер в папку 'media' асинхронно (без перезагрузки)"""
# Скорее всего это можно сделать только с помощью Ajax



"""
accounts.MyUser
accounts.Profile

image_app.MediaStorage
fields:
- image
- created
- updated
- user (ForeignKey)

"""