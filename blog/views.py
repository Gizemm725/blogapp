from django.http import HttpResponse
from django.shortcuts import render
from blog.models import Blog


data={
    "blogs": [
        {
            "id":1,
            "title":"komple web geliştime",
            "image":"4.webp",
             "is_active":True,
             "is_home":False,
             "description":"çok iyi bir kurs"
        },

           {
            "id":2,
            "title":"python kursu",
            "image":"2.webp",
             "is_active":True,
              "is_home":True,
             "description":"çok iyi bir kurs"
        },

           {
            "id":3,
            "title":"Django kursu",
            "image":"3.webp",
             "is_active":False,
              "is_home":True,
             "description":"çok iyi bir kurs"
        },
    ]
}

# views.py'da context ekleyin
def index(request):
    context = {
        "blogs":Blog.objects.all
    }
    return render(request, "blog/index.html", context)

def blogs(request):
    
    return render(request,"blog/blogs.html")
def blog_detail(request, id):
    blogs = data["blogs"]
    selectedBlog = None

    for blog in blogs:
        if blog["id"] == id:
            selectedBlog = blog
    
    return render(request, "blog/blog-details.html", {"blog": selectedBlog})