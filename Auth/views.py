from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from .forms import UserSignUpForm, EditProfileForm, UserProfileForm
from Auth.models import UserProfile


# Create your views here.

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)

            return redirect('/')
        else:
            messages.success(request, ('username or password is incorrect'))
            return redirect('/login')
    else:
        return render(request, 'authentication/login.html')


def logout_user(request):
    logout(request)
    return redirect('/')


def register_user(request):
    if request.method == 'POST':
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('/login')

    else:
        form = UserSignUpForm()

    context = {'form': form}
    return render(request, 'authentication/register.html', context)


def edit_user_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        instance = User.objects.filter(username=request.user).first()
        profile_form = UserProfileForm(request.POST, request.FILES, instance=instance)

        if form.is_valid():
            form.save()

            messages.success(request, ('Account has been edited...'))

            return redirect('/')

        if profile_form.is_valid():
            profile_form = UserProfileForm({'user': request.user})
            profile_form.save()

            return redirect('/')
    else:
        form = EditProfileForm(instance=request.user)
        profile_form = UserProfileForm(instance=request.user)

    context = {'form': form, 'profile_form': profile_form}
    return render(request, 'authentication/edit_profile.html', context)


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, ('You have edited your password'))

            return redirect('/')

    else:
        form = PasswordChangeForm(user=request.user)

    context = {'form': form}
    return render(request, 'authentication/change_password.html', context)


def show_users(request):
    users = User.objects.all()

    return render(request, "base.html", {'users': users})


def view_profile(request, pk=None):
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user
    return render(request, "user_profile.html", {'user': user})


def change_user_profile(request):
    if request.method == 'POST':
        profile_form = UserProfileForm(request.POST, request.FILES)
        if profile_form.is_valid():
            profile_form.save()

            return redirect('/')
        return render(request, 'authentication/edit_profile.html', {"profile_form": profile_form})
