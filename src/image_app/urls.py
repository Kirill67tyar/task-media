from django.urls import path
from image_app.views import check, profile, experiment

app_name = 'image_app'

urlpatterns = [
    path('', check, name='check'),
    path('profile/', profile, name='profile'),
    path('experiment/', experiment, name='experiment'),

]