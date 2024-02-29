import json
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

    def getPostsJSON(self) -> dict:
        posts = Post.objects.select_related('author')
        datas = []
        for p in posts:
            data = {
                "title":p.title,
                "content": p.content,
                }
            if p.author != None:
                au = {
                    "author_name": p.author.name,
                    "author_email": p.author.email,
                    }
                data.update(au)
            datas.append(data)
            j = json.dumps(datas)
        return j




