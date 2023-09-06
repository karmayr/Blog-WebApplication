from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from .models import Blog,Contact,Profile
from django.urls import reverse
from django.core.paginator import Paginator
from .forms import *
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required



# Create your views here.
def home(request):
    ins = Blog.objects.all()
    context = {"blogs" : ins }
    # print(context)
    return render(request,'index.html',context)

def login_view(request):
    return render(request,'login_page.html')

def logout_view(request):
    logout(request)
    return render(request,'login_page.html')

def signupview(request):
    return render(request,'signup.html')


@login_required(login_url='login')
def blog(request):
    objs = Blog.objects.filter(user = request.user)
    paginator = Paginator(objs, 4)  # Show 3 blogs per page.
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {'page_obj' : page_obj , 'blog' : objs}

    return render(request,'bloghome.html',context)

@login_required(login_url='login')
def blogpost(request,slug):
    ins = Blog.objects.filter(slug=slug).first()
    context = {'data' : ins}
    return render(request,'blogpost.html',context)

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        number = request.POST.get('phone')
        desc = request.POST.get('views')

        obj = Contact(name=name,email=email,number=number,desc=desc)
        obj.save() 
         
    return render(request,'contact.html')

def search(request):
    query = request.GET.get('searchtitle')
    results = Blog.objects.filter(title__icontains=query) 

    context = {
        'blogs': results,
        'query': query,
    }
    # print(context)
    return render(request,'searchresults.html',context)



@login_required(login_url='login')
def AddBlog(request):
    context = {'form' : FroalaBlogForm}
    try:
        if request.method == 'POST':
            form = FroalaBlogForm(request.POST)
            image = request.FILES['file']
            title = request.POST.get('title')
            user = request.user
        
            if form.is_valid():
                content = form.cleaned_data['content']
                Blog.objects.create(user=user,title=title,content = content,upload=image)
                return redirect('blog')


    except Exception as e:
       print (e)
    return render(request,'addblog.html',context)

@login_required(login_url='login')
def MyBlogs(request):
    user_objs = Blog.objects.filter(user=request.user)
    context = {'user_blogs' : user_objs} 
    return render(request,'my_blogs.html', context)

@login_required(login_url='login')
def UpdateBlog(request,slug):
    context = {}
    try:
        blog = Blog.objects.get(slug=slug)
        if blog.user != request.user:
            return HttpResponseRedirect(reverse('myblogs'))
        old_data_dict = {
            'content' : blog.content,
            'title' : blog.title,
            'image' : blog.upload
        }
        form = FroalaBlogForm( initial = old_data_dict)
        
        if request.method == 'POST':
            form = FroalaBlogForm(request.POST)
            image = request.FILES['file']
            title = request.POST.get('title')
            user = request.user
        
            if form.is_valid():
                content = form.cleaned_data['content']
                blog.title = title
                blog.upload =image
                blog.content =content
                blog.save()
                return HttpResponseRedirect(reverse('myblogs'))
        context = {'blog' : blog , 'form' : form}
    except Exception as e:
        print(e)
    return render(request,'update_blog.html',context)

@login_required(login_url='login')
def DeleteBlog(request,slug):
    blog = Blog.objects.get(slug=slug)
    if blog.user == request.user:
        blog.delete()
    else:
        return HttpResponse("Unauthorised action")
    return HttpResponseRedirect(reverse('myblogs'))

def verify(request,token):
    try:
        profile = Profile.objects.filter(token = token).first()

        if profile:
            profile.verified = True
            profile.save()
        return redirect('login')
    
    except Exception as e:
        print(e)
    return HttpResponseRedirect(reverse('/'))