from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect, reverse
from accounts.forms import RegisterModelForm, LoginForm




def register_user(request):
    # if not request.user.is_authenticated:
    form = RegisterModelForm(request.POST or None)
    if form.is_valid():
        data = form.cleaned_data
        password = data['password2']
        user = form.save(commit=False)
        user.set_password(password)
        user.save()
        return redirect(reverse('accounts:login'))
    return render(request, 'accounts/login_or_register.html', context={'form': form,'login_t_f': False,})
    # else:
    #     return redirect(reverse('image_app:profile'))
    





def login_user(request):
    # if not request.user.is_authenticated:
    form = LoginForm(request.POST or None)
    if form.is_valid():
        data = form.cleaned_data
        email = data['email']
        password = data['password']
        user = authenticate(request, email=email, password=password)
        login(request, user)
        return redirect(reverse('image_app:check'))
    return render(request, 'accounts/login_or_register.html', context={'form': form, 'login_t_f': True,})
    # else:
    #     return redirect(reverse('image_app:profile'))




def logout_user(request):
    logout(request)
    return redirect(reverse('accounts:login'))










