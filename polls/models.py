from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    content = models.CharField()

class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
