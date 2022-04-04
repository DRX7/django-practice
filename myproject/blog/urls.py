from django.urls import path


from blog.views import (ArticleDetail,
                        ArticleList,
                        ArticlePreview,
                        AuthorList,
                        CategoryList, SearchList
                                        )

# from django.conf import settings
# from django.conf.urls.static import static




app_name = 'blog'
urlpatterns = [
    path ('',ArticleList.as_view(),name='home'),
    path ('page/<int:page>' , ArticleList.as_view(), name='home'),
    path ('detail/<slug:slug>' , ArticleDetail.as_view() , name='detail'),
    path ('preview/<int:pk>' , ArticlePreview.as_view() , name='preview'),
    path ('category/<slug:slug>' , CategoryList.as_view() , name='categorylist'),
    path ('category/<slug:slug>/page/<int:page>' , CategoryList.as_view() , name='categorylisti'),
    path ('author/<slug:username>' , AuthorList.as_view() , name='author'),
    path ('search/' , SearchList.as_view() , name='search'),
    path ('category/page/<int:page>' , SearchList.as_view() , name='search'),
]



# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
