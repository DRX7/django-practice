from django.db import models
from django.shortcuts import render , get_object_or_404
from django.views.generic import DetailView , ListView , CreateView , UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from account.mixins import FieldsMixin , FormValidMixin , ArticleAccessMixin

from blog.models import Article
# Create your views here.


class HomeAcc(LoginRequiredMixin,ListView):
    template_name = 'registration/home.html'

    def queryset(self):
        if self.request.user.is_superuser:
            return Article.objects.all()
        else:
            return Article.objects.filter(author=self.request.user)
    

class ArticleCreate(LoginRequiredMixin,FieldsMixin,FormValidMixin , CreateView):
    model = Article
    template_name = "registration/article_create_update.html"


class ArticleUpdate(ArticleAccessMixin,FieldsMixin,FormValidMixin , UpdateView):
    model = Article
    template_name = "registration/article_create_update.html"
