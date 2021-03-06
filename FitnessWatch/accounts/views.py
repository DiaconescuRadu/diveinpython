from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect
from accounts.forms import SignUpForm
from django.contrib.auth.models import User

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('boards')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def all_accounts(request):
    return render(request, 'list_users.html', {'users': User.objects.all()})


