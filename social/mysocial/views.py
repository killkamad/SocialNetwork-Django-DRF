from .models import Post, Like
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .forms import PostForm, UserRegisterForm, EditProfileForm
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib import messages

from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializers import PostSerializer
from .mixins import LikedMixin

from rest_framework import generics, permissions
from .permissions import IsOwner




# Создание постов, изменение, просмотр
def com_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'mysocial/com_list.html', {'posts': posts})


def com_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'mysocial/com_detail.html', {'post': post})

def com_new(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES or None)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            # messages.success(request, f'Вы добавили новую публикацию')
            return redirect('com_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'mysocial/com_edit.html', {'form': form})


def com_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST or None, request.FILES or None, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            # messages.success(request, f'Вы изменили публикацию')
            return redirect('com_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'mysocial/com_edit.html', {'form': form})

#Форма регистрации


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            # messages.success(request, f'Вы зарегестрировались как {username} и можете войти в свой аккаунт!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'mysocial/register.html', {'form': form})


# Profile view
def view_profile(request, pk=None):
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user
    args = {'user': user}
    return render(request, 'mysocial/profile.html', args)

def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect(view_profile)
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'mysocial/edit_profile.html', args)

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('view_profile')
        else:
            return redirect('change_password')
    else:
        form = PasswordChangeForm(user=request.user)

        args = {'form': form}
        return render(request, 'mysocial/change_password.html', args)

#Лайки

User = get_user_model()
def add_like(obj, user):
    obj_type = ContentType.objects.get_for_model(obj)
    like, is_created = Like.objects.get_or_create(
        content_type=obj_type, object_id=obj.id, user=user)
    return like
def remove_like(obj, user):
    obj_type = ContentType.objects.get_for_model(obj)
    Like.objects.filter(
        content_type=obj_type, object_id=obj.id, user=user
    ).delete()
def is_fan(obj, user) -> bool:
    if not user.is_authenticated:
        return False
    obj_type = ContentType.objects.get_for_model(obj)
    likes = Like.objects.filter(
        content_type=obj_type, object_id=obj.id, user=user)
    return likes.exists()
def get_fans(obj):
    obj_type = ContentType.objects.get_for_model(obj)
    return User.objects.filter(
        likes__content_type=obj_type, likes__object_id=obj.id)

class PostViewSet(LikedMixin,viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # permission_classes = (IsAuthenticatedOrReadOnly,)
    permission_classes = (
        permissions.IsAuthenticated, IsOwner)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
