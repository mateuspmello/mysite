from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

class Post(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    content = models.CharField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)


