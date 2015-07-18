from django.shortcuts import redirect, render
from django.contrib.auth import logout


def login_view(request):
    if request.user.is_authenticated():
        return redirect('/')
    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('/')
