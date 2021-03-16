from django.contrib import admin
from .models import ImageStorage
from simple_history.admin import SimpleHistoryAdmin


class ImageStorageAdmin(SimpleHistoryAdmin):

    fields = 'id', 'user', 'timestamp', 'image', 'history',
    readonly_fields = 'id', 'timestamp', 'history',
    list_display = 'id', 'timestamp', #'status',
    history_list_display = ["status",]

admin.site.register(ImageStorage, ImageStorageAdmin)

