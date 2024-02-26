from django.http import HttpResponse
from django.template import loader
from django.core import serializers
from .models import Post

def index(request):
    template = loader.get_template("index.html")
    return HttpResponse(template.render())

def posts(request):
    posts = Post.objects.all()
    data = serializers.serialize('json', posts)
    return HttpResponse(data)