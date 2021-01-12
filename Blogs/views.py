from django.shortcuts import render, get_object_or_404
from .models import Blog_Post

def BlogPage(request):
    
    Allblogs = Blog_Post.objects
    return render(request, 'Blogs/BlogPage.html', {'Blogs' : Allblogs})

def fullBlogPage(request, blog_id):
    fullBlog = get_object_or_404(Blog_Post, pk=blog_id)
    return render(request, 'Blogs/fullBlog.html', {'Blog' : fullBlog})