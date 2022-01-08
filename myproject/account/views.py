from django.db import models
from django.shortcuts import render , get_object_or_404
from django.views.generic import DetailView , ListView

from blog.models import Article
# Create your views here.


class HomeAcc(ListView):
    queryset = Article.objects.all()
    template_name = 'registration/home.html'
