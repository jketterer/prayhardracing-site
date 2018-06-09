from django.db import models

# Create your models here.
class Driver(models.Model):
    name = models.CharField(max_length=20)
    bio = models.TextField(max_length=200)
    picture = models.ImageField(upload_to="driver_images/")
    junior = models.BooleanField()
    def __str__(self):
        return self.name

class About(models.Model):
    info = models.TextField(max_length=1000)
    picture = models.ImageField(upload_to="about_images/")
