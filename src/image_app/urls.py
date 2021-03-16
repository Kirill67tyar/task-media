from django.urls import path
from image_app.views import check

app_name = 'image_app'

urlpatterns = [
    path('', check, name='check'),

]