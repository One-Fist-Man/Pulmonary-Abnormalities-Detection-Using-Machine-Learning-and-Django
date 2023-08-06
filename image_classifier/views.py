import os
from django.shortcuts import render
from django.conf import settings
from .forms import ImageUploadForm
from .utils import classify_image

def classify(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            result = classify_image(image)
            return render(request, 'result.html', {'result': result})
    else:
        form = ImageUploadForm()
    return render(request, 'upload.html', {'form': form})
