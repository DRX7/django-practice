from django.contrib.auth import views
from django.urls import path

from account.views import (ArticleCreate,
                            ArticleDelete,
                            HomeAcc ,
                            ArticleUpdate,
                            Profile
                                    )

app_name = 'account'

urlpatterns = [
    path('account/' , HomeAcc.as_view() , name='home'),
    path('account/article/create' , ArticleCreate.as_view() , name='article-create'),
    path('account/article/update/<int:pk>' , ArticleUpdate.as_view() , name='article-update'),
    path('account/article/delete/<int:pk>' , ArticleDelete.as_view() , name='article-delete'),
    path('account/profile/' , Profile.as_view() , name='profile'),
]
