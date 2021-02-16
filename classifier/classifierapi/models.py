from django.db import models
from keras.preprocessing.image import load_img, img_to_array 
from keras.preprocessing import image
from tensorflow.keras.applications.inception_resnet_v2 import InceptionResNetV2, decode_predictions, preprocess_input
import numpy as np

class Image(models.Model):
    picture = models.ImageField()
    classified = models.CharField(max_length=255)
    uploaded = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.classified

    def save(self, *args, **kwargs):
        try:
            img = load_img(self.picture.path, target_size=(300, 300))
            img_array = img_to_array(img)
            img_array = img_array.reshape(1, 300, 300, 3)
            prep = preprocess_input(img_array)
            model = InceptionResNetV2(weights='imagenet')
            prediction = model.predict(prep)
            decoded = decode_predictions(prediction)[0][0][1]
            self.classified = str(decoded)
            print('Success')
        except Exception as e:
            print('Error: ' + e)
        super().save(*args, **kwargs)