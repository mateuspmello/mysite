from django.http import HttpResponse
from django.template import loader
from polls.serializers import PostSerializer, AuthorSerializer
from .models import *
from rest_framework import viewsets


def index(request):
    template = loader.get_template("index.html")
    return HttpResponse(template.render())

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    http_method_names = ['get','post','retrieve','put','patch']

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    http_method_names = ['get','post','retrieve','put','patch']