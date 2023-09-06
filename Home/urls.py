
from django.urls import path
from .views import *
urlpatterns = [
    path("",home,name='home'),
    path("contact/",contact,name='contact'),
    path("blog/",blog,name='blog'),
    path("blogpost/<str:slug>/",blogpost,name='blogpost'),
    path("search/",search,name="search"),
    path("login/",login_view,name='login'),
    path("logout/",logout_view,name='logout_view'),
    path("signup/",signupview,name='signup'),
    path("addblog/",AddBlog,name='addblog'),
    path("my-blogs/",MyBlogs,name='myblogs'),
    path("update-blog/<slug>/",UpdateBlog,name='blog_update'),
    path("delete-blog/<slug>/",DeleteBlog,name='blog_delete'),
    path('verify/<token>/',verify,name='verify')
]