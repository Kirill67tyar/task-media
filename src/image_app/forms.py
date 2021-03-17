from django import forms
from image_app.models import ImageStorage



class LoadImageForm(forms.ModelForm):

    class Meta:
        model = ImageStorage
        fields = 'image',
        widgets = {'image': forms.FileInput(attrs={'class': 'form-control',})}

