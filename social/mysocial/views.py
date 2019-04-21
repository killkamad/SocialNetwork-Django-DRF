from .models import Post
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .forms import PostForm, UserRegisterForm, EditProfileForm
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib import messages



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


#Friendlist
# def change_friends(request,operation,pk):
#     friend = Friend.objects.get(current_user=request.user)
#     friendss = friend.users.all()
#     friend= User.Objects.get(pk=pk)
#     if operation == 'add':
#         Friend.make_friend(request.user, friend)
#     elif operation == 'remove':
#         Friend.lose_friend(request.user, friend)
#     return render(request, 'mysocial/friend_list.html')

# def change_friends(request, operation, pk):
#     friend = User.objects.get(pk=pk)
#     if operation == 'add':
#         Friend.make_friend(request.user, friend)
#     elif operation == 'remove':
#         Friend.lose_friend(request.user, friend)
#     return render(request, 'mysocial/friend_list.html')

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

#Friendlist

# from django.shortcuts import render, get_object_or_404, redirect
# from .models import UserProfile
# from django.contrib.auth.models import User
# from .models import Friend
# from django.contrib.auth.decorators import login_required
# #
# # @login_required
# # def add_or_remove_friends(request, username, verb):
# #     n_f = get_object_or_404(User, username=username)
# #     owner = request.user.userprofile
# #     new_friend = UserProfile.objects.get(user=n_f)
# #
# #     if verb == "add":
# #         new_friend.followers.add(owner)
# #         Friend.make_friend(owner, new_friend)
# #     else:
# #         new_friend.followers.remove(owner)
# #         Friend.remove_friend(owner, new_friend)
# #
# #     return redirect(new_friend.get_absolute_url())
# #
# # def list_friends(request):
# #     friend_object, created = Friend.objects.get_or_create(current_user=request.user.userprofile)
# #     friends = [friend for friend in friend_object.users.all() if friend != request.user.userprofile]
# #     return render(request, 'friend_list.html', {"friends":friends})

# from django.conf import settings
# from django.contrib.auth import get_user_model
# from django.http import HttpResponseRedirect
# from django.shortcuts import render, get_object_or_404
#
# from .models import Profile, FriendRequest
#
# User = get_user_model()
#
# def users_list(request):
# 	users = Profile.objects.exclude(user=request.user)
# 	context = {
# 		'users': users
# 	}
# 	return render(request, "mysocial/friend_list.html", context)
#
# def send_friend_request(request, id):
# 	if request.user.is_authenticated():
# 		user = get_object_or_404(User, id=id)
# 		frequest, created = FriendRequest.objects.get_or_create(
# 			from_user=request.user,
# 			to_user=user)
# 		return HttpResponseRedirect('/users')
#
# def cancel_friend_request(request, id):
# 	if request.user.is_authenticated():
# 		user = get_object_or_404(User, id=id)
# 		frequest = FriendRequest.objects.filter(
# 			from_user=request.user,
# 			to_user=user).first()
# 		frequest.delete()
# 		return HttpResponseRedirect('/users')
#
# def accept_friend_request(request, id):
# 	from_user = get_object_or_404(User, id=id)
# 	frequest = FriendRequest.objects.filter(from_user=from_user, to_user=request.user).first()
# 	user1 = frequest.to_user
# 	user2 = from_user
# 	user1.profile.friends.add(user2.profile)
# 	user2.profile.friends.add(user1.profile)
# 	frequest.delete()
# 	return HttpResponseRedirect('/users/{}'.format(request.user.profile.slug))
#
# def delete_friend_request(request, id):
# 	from_user = get_object_or_404(User, id=id)
# 	frequest = FriendRequest.objects.filter(from_user=from_user, to_user=request.user).first()
# 	frequest.delete()
# 	return HttpResponseRedirect('/users/{}'.format(request.user.profile.slug))
#
# def profile_view(request, slug):
# 	p = Profile.objects.filter(slug=slug).first()
# 	u = p.user
# 	sent_friend_requests = FriendRequest.objects.filter(from_user=p.user)
# 	rec_friend_requests = FriendRequest.objects.filter(to_user=p.user)
#
# 	friends = p.friends.all()
#
# 	# is this user our friend
# 	button_status = 'none'
# 	if p not in request.user.profile.friends.all():
# 		button_status = 'not_friend'
#
# 		# if we have sent him a friend request
# 		if len(FriendRequest.objects.filter(
# 			from_user=request.user).filter(to_user=p.user)) == 1:
# 				button_status = 'friend_request_sent'
#
# 	context = {
# 		'u': u,
# 		'button_status': button_status,
# 		'friends_list': friends,
# 		'sent_friend_requests': sent_friend_requests,
# 		'rec_friend_requests': rec_friend_requests
# 	}
#
# 	return render(request, "mysocial/prof.html", context)