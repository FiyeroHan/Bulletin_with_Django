from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

class Reple(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    content = models.TextField()