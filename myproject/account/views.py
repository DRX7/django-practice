from pyexpat import model
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
from django.contrib.auth.views import LoginView , PasswordChangeView

from account.mixins import (FieldsMixin ,
							FormValidMixin ,
							ArticleAccessMixin,
							ArticleAccessDeleteMixin,
							AuthorAccessMixin)

from django.urls import reverse_lazy
from blog.models import Article
from account.forms import ProfileForm
# Create your views here.


class HomeAcc(AuthorAccessMixin,ListView):
	template_name = 'registration/home.html'

	def queryset(self):
		if self.request.user.is_superuser:
			return Article.objects.all()
		else:
			return Article.objects.filter(author=self.request.user)
	

class ArticleCreate(AuthorAccessMixin,FieldsMixin,FormValidMixin , CreateView):
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






from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import SignupForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token

from django.core.mail import EmailMessage


class Register(CreateView):
	form_class = SignupForm
	template_name = "registration/register.html"

	def form_valid(self , form):

		user = form.save(commit=False)
		user.is_active = False
		user.save()
		current_site = get_current_site(self.request)
		mail_subject = 'فعالسازی حساب شما'
		message = render_to_string('registration/acc_active_email.html', {
				'user': user,
				'domain': current_site.domain,
				'uid':urlsafe_base64_encode(force_bytes(user.pk)),
				'token':account_activation_token.make_token(user),
			})
		to_email = form.cleaned_data.get('email')
		email = EmailMessage(
						mail_subject, message, to=[to_email]
			)
		email.send()
		return HttpResponse('لطفا آدرس ایمیل خود را برای تکمیل ثبت نام تایید کنید')



def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        # return redirect('home')
        return HttpResponse('با تشکر از شما برای تایید ایمیل شما. اکنون می توانید به حساب کاربری خود وارد شوید.')
    else:
        return HttpResponse('لینک فعال سازی نامعتبر است!')





		
	
