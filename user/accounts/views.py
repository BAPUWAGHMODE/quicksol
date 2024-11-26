from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from accounts.forms import RegistrationForm, LoginForm
from .models import User, Chat
from django.db import models


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('user_list')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


@login_required
def user_list(request):
    users = User.objects.exclude(id=request.user.id)
    return render(request, 'user_list.html', {'users': users})


@login_required
def chat_window(request, user_id):
    other_user = get_object_or_404(User, id=user_id)
    chats = Chat.objects.filter(
        (models.Q(sender=request.user) & models.Q(receiver=other_user)) |
        (models.Q(sender=other_user) & models.Q(receiver=request.user))
    ).order_by('timestamp')


    if request.method == 'POST':
        message = request.POST.get('message')
        Chat.objects.create(sender=request.user, receiver=other_user, message=message)

    return render(request, 'chat.html', {'chats': chats, 'other_user': other_user})

