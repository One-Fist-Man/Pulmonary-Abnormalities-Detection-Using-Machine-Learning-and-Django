from django import forms
from image_classifier.models import UploadedImage

class ImageUploadForm2(forms.ModelForm):
    class Meta:
        model = UploadedImage
        fields = ('image',)

class ImageUploadForm(forms.Form):
    image = forms.ImageField()
