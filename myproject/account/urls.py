from django.contrib.auth import views
from django.urls import path

from account.views import (ArticleCreate,
                            ArticleDelete,
                            HomeAcc ,
                            ArticleUpdate,
                            Login, PasswordChange,
                            Profile
                                    )

app_name = 'account'
urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),

    path('account/password_change/', PasswordChange.as_view(), name='password_change'),
    path('account/password_change/done/', views.PasswordChangeDoneView.as_view(), name='password_change_done'),

    # path('password_reset/', views.PasswordResetView.as_view(), name='password_reset'),
    # path('password_reset/done/', views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    # path('reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # path('reset/done/', views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]

urlpatterns += [
    path('account/' , HomeAcc.as_view() , name='home'),
    path('account/article/create' , ArticleCreate.as_view() , name='article-create'),
    path('account/article/update/<int:pk>' , ArticleUpdate.as_view() , name='article-update'),
    path('account/article/delete/<int:pk>' , ArticleDelete.as_view() , name='article-delete'),
    path('account/profile/' , Profile.as_view() , name='profile'),
]
