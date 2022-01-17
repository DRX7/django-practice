from django.urls import reverse
from dataclasses import fields
from django.db import models
from django.http import request
from django.shortcuts import render , get_object_or_404
from django.views.generic import (  DetailView ,
                                    ListView ,
                                    CreateView ,
                                    UpdateView ,
                                    DeleteView)

from django.contrib.auth.mixins import LoginRequiredMixin
from account.models import User
from django.contrib.auth.views import LoginView

from account.mixins import (FieldsMixin ,
                            FormValidMixin ,
                            ArticleAccessMixin,
                            ArticleAccessDeleteMixin)

from django.urls import reverse_lazy
from blog.models import Article
from account.forms import ProfileForm
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


class Profile(LoginRequiredMixin ,UpdateView):
    
    form_class = ProfileForm
    template_name = "registration/profile.html"
    success_url = reverse_lazy("account:profile")

    def get_object(self):
        return User.objects.get(pk = self.request.user.pk)

    
    def get_form_kwargs(self):
        kwargs =  super( Profile,self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class Login(LoginView):

    def get_success_url(self):
        user = self.request.user
        if user.is_superuser or user.is_author:
            return reverse("account:home")
        else:
            return reverse("account:profile")
        
    
