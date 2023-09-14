from django.shortcuts import render
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from django.contrib import messages
import os
from django.shortcuts import render
from django.conf import settings
from .forms import ImageUploadForm
from .utils import classify_image
import tensorflow as tf
from PIL import Image
from .forms import ImageUploadForm,ImageUploadForm2
from image_classifier.models import UploadedImage
def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm2(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('image_display')
    else:
        form = ImageUploadForm()
    return render(request, 'upload_image.html', {'form': form})

def display_image(request):
    images = UploadedImage.objects.all()
    return render(request, 'result.html', {'images': images})

def classify(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            result = classify_image(image)
            return render(request, 'result.html',{'result': result})
    else:
        form = ImageUploadForm()
    return render(request, 'upload.html', {'form': form})

def index(request):
    return render(request, 'index.html')
def home(request):
    return render(request, 'home.html')

def predict(request):
    return render(request, 'predict.html')

def result(request):
    return render(request, 'predict.html')
