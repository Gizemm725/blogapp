from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="home"),
    path("blogs/", views.blogs, name="blogs"),
    path("blogs/<int:id>/", views.blog_detail, name="blog_detail"),
]






