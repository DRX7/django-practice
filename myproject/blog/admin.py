from django.contrib import admin
from blog.models import Article, Category


# Action Admin Panel 

@admin.action(description='منتشر کردن موارد انتخاب شده')
def make_published(modeladmin, request, queryset):
    queryset.update(status='p')



@admin.action(description='پیش نویس کردن موارد انتخاب شده')
def make_drafted(modeladmin, request, queryset):
    queryset.update(status='d')
















# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title' , 'slug' , 'parent','position' , 'status']
    list_filter = ['status']
    search_fields = ['title']



class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title' , 'slug','image_tag','author' , 'publish' , 'status' , 'str_category']
    list_filter = ['publish']
    search_fields = ['title' , 'description']
    actions = [make_published, make_drafted]



admin.site.register(Article , ArticleAdmin)
admin.site.register(Category , CategoryAdmin)
