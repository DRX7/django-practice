from django.db import models
from django.shortcuts import render , get_object_or_404
from django.views.generic import DetailView , ListView , CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from blog.models import Article
# Create your views here.


class HomeAcc(LoginRequiredMixin,ListView):
    template_name = 'registration/home.html'

    def queryset(self):
        if self.request.user.is_superuser:
            return Article.objects.all()
        else:
            return Article.objects.filter(author=self.request.user)
    

class ArticleCreate(LoginRequiredMixin , CreateView):
    model = Article
    fields = ['author' , 'title','slug' , 'category' , 'description' , 'image' , 'publish' , 'status']
    template_name = "registration/article_create_update.html"
