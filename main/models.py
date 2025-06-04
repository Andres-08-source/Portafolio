from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    link = models.URLField()
    date = models.DateField(auto_now_add=False)

    def __str__(self):
        return self.title