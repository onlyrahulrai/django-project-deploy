from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=198)
    description = models.TextField()
    image = models.ImageField(upload_to="posts/")

    def __str__(self):
        return self.title