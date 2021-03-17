from django.contrib import admin
from image_app.models import ImageStorage, History
from django.utils.safestring import mark_safe


class ImageStorageAdmin(admin.ModelAdmin):

    fields = 'id', 'user', 'timestamp', 'image', #'history',
    readonly_fields = 'id', 'timestamp', #'history',
    list_display = 'id', 'timestamp', 'get_image', #'status',

    def get_image(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="50">')
        return '--/--'




class HistoryAdmin(admin.ModelAdmin):

    fields = 'image', 'cause', 'timestamp',
    readonly_fields = 'timestamp',


admin.site.register(ImageStorage, ImageStorageAdmin)
admin.site.register(History, HistoryAdmin)

