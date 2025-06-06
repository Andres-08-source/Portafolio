from django.db import models
from cloudinary.models import CloudinaryField


# Create your models here.
class Technology(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    link = models.URLField()
    image = CloudinaryField('image', null=True, blank=True)
    date = models.DateField(auto_now_add=False)
    technologies = models.ManyToManyField(Technology)  # ¡Aquí la magia!


    def __str__(self):
        return self.title

