from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.
class UserData(models.Model):
    pattern = models.CharField(max_length=10, primary_key=True, editable=False)
    text = models.TextField(null=True)
    secret_key = models.CharField(max_length=10, blank=True, null=True)
    text_encrypt = models.BinaryField(null=True, blank=True)

class Post(models.Model):
    title = models.CharField(max_length=200)
    
    


