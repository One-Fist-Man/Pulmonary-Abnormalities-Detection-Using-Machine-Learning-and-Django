import tensorflow as tf
from PIL import Image
from django.conf import settings
import os

def classify_image(image):
    model_path = os.path.join(settings.BASE_DIR, 'model_inception.h5')
    model = tf.keras.models.load_model(model_path)

    img = Image.open(image)
    img = img.resize((224, 224))  # Resize as needed by your model
    img_array = tf.keras.preprocessing.image.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0)  # Add batch dimension
    img_array /= 255.0  # Normalize

    predictions = model.predict(img_array)
    class_index = tf.argmax(predictions[0])
    class_label = "Class Label"  # Replace with your actual class labels

    return class_label
