from . import views
from django.urls import path

# paths within the fp_blog app
urlpatterns = [
    path('', views.ArticleList, name='home'),
    path('<slug:slug>/', views.ArticleDetail.as_view(), name='article_detail'),
    path('bookmark/<slug:slug>', views.ArticleBookmark.as_view(),
         name='article_bookmark'),
    path('like/<slug:slug>', views.ArticleLike.as_view(), name='article_like'),
    path('comment/<slug:slug>', views.ArticleComment.as_view(),
         name='article_comment'),
]

# Error handlers for site errors
handler404 = 'fp_blog.views.error_404'
handler500 = 'fp_blog.views.error_500'
handler403 = 'fp_blog.views.error_403'
handler400 = 'fp_blog.views.error_400'
