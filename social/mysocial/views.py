from .models import Post
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .forms import PostForm, UserRegisterForm
from django.shortcuts import redirect
# from django.contrib import messages



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