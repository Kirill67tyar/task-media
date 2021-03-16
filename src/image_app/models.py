from django.db.models import (Model, ImageField, DateTimeField, ForeignKey, CASCADE)
from django.db import models
from simple_history.models import HistoricalRecords
from media_service.settings import AUTH_USER_MODEL
from django.conf import settings

User = settings.AUTH_USER_MODEL




class ImageStorage(Model):

    user = ForeignKey(User, on_delete=CASCADE, related_name='images_created')
    image = ImageField(upload_to='images/%Y/%m/%d', blank=True, verbose_name='Изображение')
    timestamp = DateTimeField(auto_now_add=True)
    history = HistoricalRecords()

    class Meta:
        verbose_name = 'Хранилище изоборажений'
        verbose_name_plural = 'Хранилище изоборажений'



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