from django.shortcuts import render, redirect
from .forms import RegistrationFrom, PostForm
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import login, logout, authenticate

from .models import Post
from django.contrib.auth.models import User, Group
# Create your views here.


@login_required(login_url='/login')
def home(request):
    """home view: render's home template"""
    posts = Post.objects.all()

    if request.method == 'POST':
        post_id = request.POST.get('post-id')
        user_id = request.POST.get('user-id')
        if post_id:
            post = Post.objects.get(id=post_id)
            if post and (post.author == request.user or request.user.has_perm("main.delete_post")):
                post.delete()
        elif user_id:
            user = User.objects.get(id=user_id)
            if user and request.user.is_staff:
                group= Group.objects.all()
                for g in group:
                    g.user_set.remove(user)
            has_create_post_permission = request.user.has_perm('main.create_post')
                

    return render(request, 'main/home.html', {"posts": posts})


@login_required(login_url='/login')
@permission_required("main.add_post", login_url="/login", raise_exception=True)
def create_post(request):
    """create post view"""
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('/home')
    else:
        form = PostForm()

    return render(request, 'main/create_post.html', {"form": form})


def sign_up(request):
    """sign_up view: create a new user with register form"""
    if request.method == 'POST':
        form = RegistrationFrom(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/home')
    else:
        form = RegistrationFrom()

    return render(request, 'registration/sign_up.html', {"form": form})
