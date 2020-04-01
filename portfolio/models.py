from django.db import models

# Create your models here.
class Project(models.Model):
    Title=models.CharField(max_length=250)
    Description=models.CharField(max_length=250)
    Image=models.ImageField(upload_to='portfolio/images')
    URL=models.URLField(blank=True)
