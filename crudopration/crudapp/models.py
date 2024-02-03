from django.db import models

# Create your models here.

class Post(models.Model):
    post_name =  models.CharField(max_length = 100)
    post_description =  models.TextField()

    def __str__(self):
        return self.post_name