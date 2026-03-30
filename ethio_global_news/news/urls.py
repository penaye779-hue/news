from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('news/<int:pk>/', views.news_detail, name='news_detail'),
    path('news_list/', views.news_list, name='news_list'),
    path('news/create/', views.news_create, name='news_create'),
    path('edit/<int:news_id>/', views.news_edit, name='news_edit'),
    path('delete/<int:news_id>/', views.news_delete, name='news_delete'),
    path('category/<int:category_id>/', views.category_news, name='category_news'),
    path('subscribe/', views.subscribe, name='subscribe'),
]