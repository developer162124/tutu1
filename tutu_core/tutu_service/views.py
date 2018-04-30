from django.contrib import auth
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User


def index(request):
    context = {}
    if request.user.is_authenticated():
        context['auth'] = request.user
    return render(request, "tutu_service/index.html", context)


def register(request):
    if request.POST:
        user = User.objects.create_user(
                password=request.POST["pwd"],
                username=request.POST["name"],
        )
        user.save()
        return redirect(reverse('tutu_service:index'))
    else:
        return render(request, "tutu_service/register.html")


def login(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            auth.login(request, user)
            return redirect(reverse('tutu_service:index'))
        else:
            return redirect(reverse('tutu_service:index'))
    else:
        return render(request, "tutu_service/login.html")


def logout(request):
    auth.logout(request)
    return redirect(reverse('tutu_service:index'))


def products(request):
    context = {}
    return render(request, "tutu_service/products.html", context)
