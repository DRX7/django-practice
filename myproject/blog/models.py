from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.html import format_html
# My Mangers
class ArticleManager(models.Manager):
    def published(self):
        return self.filter(status='p')


class CategoryManager(models.Manager):
    def published(self):
        return self.filter(status=True)




# Create your models here.

class Category(models.Model):
    parent = models.ForeignKey ('self' , on_delete=models.SET_NULL , blank=True , null=True, related_name='childern' ,verbose_name='زیردسته')
    title = models.CharField(max_length=256 , verbose_name='دسته بندی')
    slug = models.CharField(max_length=256 , verbose_name='آدرس دسته بندی', unique=True)
    position = models.IntegerField(verbose_name='پوزیشن')
    status = models.BooleanField(verbose_name='آيا میخواهید نمایش داده شود؟' , default=True)

    def __str__(self):
        return self.title
        
    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'

    objects = CategoryManager()




class Article(models.Model):
    CHOOSE_STATUS = (
        ('p' , 'منشر شده'),
        ('d' , 'پیش نویس')
    )
    author = models.ForeignKey(User , on_delete=models.SET_NULL , null=True , verbose_name='نویسنده',related_name='articles')
    title = models.CharField(max_length=100 , verbose_name='عنوان')
    slug = models.CharField(max_length=100 , unique=True , verbose_name='آدرس عنوان')
    category = models.ManyToManyField(Category , related_name='articles' )
    description = models.TextField(verbose_name='محتوا')
    image = models.ImageField(upload_to='image' , verbose_name='عکس')
    publish = models.DateTimeField(default=timezone.now , verbose_name='انتشار')
    status = models.CharField(choices=CHOOSE_STATUS , max_length=1 , verbose_name='وضعیت')

    class Meta:
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقالات'

    def __str__(self):
        return self.title

    def str_category(self):
        return ' ,'.join([cat.title for cat in self.category.all()])
    str_category.short_description = 'دسته بندی'


    def image_tag(self):
        return format_html(f'<img src="{self.image.url}" width=100px height=75px>')
    image_tag.short_description = 'عکس'

    def user_new_unicode(self):
        return self.get_full_name()
    

    objects = ArticleManager()

    
