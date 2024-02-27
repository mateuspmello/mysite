import json
from django.http import HttpResponse
from django.template import loader
from django.core import serializers
from .models import *

def index(request):
    template = loader.get_template("index.html")
    return HttpResponse(template.render())

def posts(request):
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
    return HttpResponse(j)

def authors(request):
    posts = Author.objects.all()
    data = serializers.serialize('json', posts)
    return HttpResponse(data)