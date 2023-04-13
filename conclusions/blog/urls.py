from . import views
from django.urls import path

urlpatterns = [
    path('pl/posts/', views.PostListPl.as_view(), name='post_list_pl'),
    path('en/posts/', views.PostListEn.as_view(), name='post_list_en'),
    path('pl/posts/<slug:slug>/', views.PostDetailPl.as_view(), name='post_detail_pl'),
    path('en/posts/<slug:slug>/', views.PostDetailEn.as_view(), name='post_detail_en'),    
]