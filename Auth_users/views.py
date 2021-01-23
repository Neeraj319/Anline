# Create your views here.
from django.shortcuts import render, HttpResponse


# Create your views here.
def login_user(request):
    return HttpResponse('login page')


def register_user(request):
    return HttpResponse("register page")


def logout_user(request):
    return HttpResponse("logout page")