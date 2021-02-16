from django.db import models

# Create your models here.
class ImgClassifier(models.Model):
    image = models.ImageField(null=True)
    prediction = models.CharField(max_length=255)
    