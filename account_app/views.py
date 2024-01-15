from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from account_app.forms import LoginForm, UserEditForm



def user_login(request):
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = User.objects.get(username=form.cleaned_data.get('username'))
            login(request, user)
            return redirect("home:main")
    else:
        form = LoginForm()
    return render(request, 'account_app/login.html', {'form': form})


def user_register(request):
    context = {'errors': []}
    if request.user.is_authenticated:
        return redirect('home:main')

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            context['errors'].append('Password does not match')
            return render(request, 'account_app/register.html', context)
        #
        # if User.objects.get(username=username):
        #     context['errors'].append('this username is exists')
        #     return render(request, 'account_app/register.html', context)

        user = User.objects.create_user(username=username, password=password1, email=email)
        print(user)
        login(request, user)
        return redirect('home:main')

    return render(request, 'account_app/register.html', {})


def user_edit(request):
    user = request.user
    form = UserEditForm(instance=user)
    if request.method == "POST":
        form = UserEditForm(data=request.POST, instance=user)
        if form.is_valid():
            form.save()
    return render(request, "account_app/edit.html", {'form': form})


def user_logout(request):
    logout(request)
    return redirect('home:main')



