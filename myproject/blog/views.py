from account.models import User
from django.views.generic import DetailView , ListView
from blog.models import Article, Category
from django.shortcuts import render , get_object_or_404
from account.mixins import ArticleAccessMixin

# Create your views here.




# def home(request):
#     context = {
#         'articles' : Article.objects.published(),
#         'category' : Category.objects.filter(status = True)
#     }
#     return render(request , 'blog/home.html' , context)

class ArticleList(ListView):
	queryset = Article.objects.published()
	template_name = 'blog/home.html'
	paginate_by = 3




class ArticleDetail(DetailView):
	template_name = 'blog/detail.html'
	def get_object(self):
		slug = self.kwargs.get('slug')
		return Article.objects.filter(status='p' , slug=slug)

class ArticlePreview(ArticleAccessMixin, DetailView):
	template_name = 'blog/detail.html'
	def get_object(self):
		pk = self.kwargs.get('pk')
		return Article.objects.filter(pk=pk)




class CategoryList(ListView):
	template_name = 'blog/category_list.html'
	paginate_by = 2
	def get_queryset(self):
		global category
		slug = self.kwargs.get('slug')
		category = get_object_or_404(Category.objects.published() , slug=slug)
		return category.articles.published()
	
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['category'] = category
		return context


class AuthorList(ListView):
	template_name = 'blog/authorlist.html'
	def get_queryset(self):
		global author
		username = self.kwargs.get('username')
		author = get_object_or_404(User, username=username)
		return author.articles.published()
	def get_context_data(self , **kwargs):
		context = super().get_context_data(**kwargs)
		context['author'] = author
		return context

	   
