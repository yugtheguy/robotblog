from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import PostForm
from .models import post
from django.core.paginator import Paginator

def edit_post(request, pk):
    post_instance = get_object_or_404(post, pk=pk, author=request.user)
    if request.method == 'POST':
        form =  PostForm(request.POST, instance=post_instance)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form=PostForm(instance=post_instance)

    return render(request, 'blogs/edit_post.html', {"form":form})


def post_show(request):
    posts = post.objects.all().order_by('-day_created') 
    paginator = Paginator(posts, 5)
    page_number=request.GET.get('page')
    page_obj= paginator.get_page(page_number)
    
    
    return render(request,'blogs/posts_show.html', {'page_obj': page_obj})


def home(request):
    return render(request, 'blogs/home.html')



def post_delete(request, pk):
    my_post=get_object_or_404(post, pk=pk)

    if my_post.author!=request.user:
        return redirect('profile')
    my_post.delete()
    

    
    return redirect('profile')


def profile(request):
    user = request.user
    posts = post.objects.filter(author=request.user).order_by('-day_created')

    return render(request, 'blogs/profile.html', {'user':user, 'posts':posts})



def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid details,Try again")
            return redirect('register')
    else:
        form = UserCreationForm()

    return render(request, 'blogs/register.html', {"form":form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid details,Try again")
            return redirect('login')
    else:
        form = AuthenticationForm()

    return render(request, 'blogs/login.html', {"form":form})

@login_required
def logout_view(request):
        logout(request)
        return redirect('home')

@login_required
def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author= request.user
            post.save()
            return redirect('home')
    else:
        form = PostForm()

    return render(request, 'blogs/add_post.html', {'form': form})


