import json
from django.http import HttpResponse
from django.template import loader
from django.core import serializers
from .models import *

def index(request):
    template = loader.get_template("index.html")
    return HttpResponse(template.render())

def posts(request):
    posts = Post().getPostsJSON()
    return HttpResponse(posts)

def authors(request):
    posts = Author.objects.all()
    data = serializers.serialize('json', posts)
    return HttpResponse(data)