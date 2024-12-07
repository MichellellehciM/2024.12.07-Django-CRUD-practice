from django.db import models


# Create your models here.
class Resume(models.Model):
    title = models.CharField(max_length=50, null=True)
    skill = models.CharField(max_length=50, null=True)
    location = models.CharField(max_length=50, null=True)
    content = models.TextField(null=True)
