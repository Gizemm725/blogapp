from django.http import HttpResponse

def index(request):
    return HttpResponse("Homepage of the Blog")

def blogs(request):
    return HttpResponse("Welcome to the Blog!")

def blog_detail(request, blog_id):
    return HttpResponse(f"Blog detail page for blog id: {blog_id}")
