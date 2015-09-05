from django.db import models

class TextAreaModel(models.Model):
    describe = models.TextField()

class ImageURLModel(models.Model):
    source = models.ImageField(upload_to='photos/')
