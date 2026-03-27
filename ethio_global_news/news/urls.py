from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('category/<int:category_id>/', views.home, name='home_by_category'),
    path('news/<int:pk>/', views.news_detail, name='news_detail'),
    path('create/', views.create_news, name='create_news'),
    path('edit/<int:id>/', views.news_edit, name='news_edit'),
    path('delete/<int:id>/', views.news_delete, name='news_delete'),
    path('news/create/', views.news_create, name='news_create'),
    path('news/', views.news_list, name='news_list'), 
    path('subscribe/', views.subscribe, name='subscribe'),
]