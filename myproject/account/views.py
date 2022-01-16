from django.db import models
from django.shortcuts import render , get_object_or_404
from django.views.generic import (  DetailView ,
                                    ListView ,
                                    CreateView ,
                                    UpdateView ,
                                    DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin

from account.mixins import (FieldsMixin ,
                            FormValidMixin ,
                            ArticleAccessMixin,
                            ArticleAccessDeleteMixin)

from django.urls import reverse_lazy
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


class ArticleDelete(ArticleAccessDeleteMixin,DeleteView):
    model = Article
    success_url = reverse_lazy('account:home')
    template_name = 'registration/article_confirm_delete.html'
    
