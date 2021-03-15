from django.urls import path
from src.image_app.views import check

app_name = 'image_app'

urlpatterns = [
    path('checking/', check, name='check'),

]