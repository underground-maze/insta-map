from django.shortcuts import redirect
from django.contrib.auth import logout


def login_view(request):
    return redirect('/login/vk-oauth2')

def logout_view(request):
    logout(request)
    return redirect('/')
