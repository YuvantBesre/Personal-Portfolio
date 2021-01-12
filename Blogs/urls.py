from django.urls import path
from . import views

urlpatterns = [
    path('', views.BlogPage, name='Blog-Page'),
    path('<int:blog_id>/', views.fullBlogPage, name='full-blog')
] 
