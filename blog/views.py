from django.shortcuts import render, get_object_or_404
from .models import Blog

def index(request):
    context = {"blogs": Blog.objects.filter(is_active=True)}
    return render(request, "blog/index.html", context)

def blogs(request):
    context = {"blogs": Blog.objects.filter(is_active=True)}
    return render(request, "blog/blogs.html", context)

def blog_detail(request, id):  # ✅ Artık slug alıyor
    blog = get_object_or_404(Blog, id=id)  # ✅ Veritabanından slug'a göre bul
    return render(request, "blog/blog-details.html", {"blog": blog})