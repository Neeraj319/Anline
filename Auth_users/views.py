# Create your views here.
from django.shortcuts import render, HttpResponse , redirect
from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.models import User, auth
from .models import Buyer
# Create your views here.
def login_user(request):
    if request.user.is_anonymous:
        if request.method == 'POST':
            user_name = request.POST.get('user_name')
            password = request.POST.get('password')
            user = authenticate(username=user_name, password=password)
            if user is not None:

                login(request, user)
                return redirect('home')
            else:
                messages.error(
                    request, 'user name or password did not matched')
                return redirect('login')
    else:

        return redirect('home')
    return render(request , 'login.html')


def register_user(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password1')
        password2 = request.POST.get('password2')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        if (first_name or last_name or username or email or phone or password or password2 or address) == '':
            messages.error(request, 'fields cant be empty')
            return redirect('register')
        else:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'username already exists')
            elif User.objects.filter(email = email).exists():
                messages.error(request, 'eamil already exists')
            elif (len(password) and len(password2)) <= 7:
                messages.error(request, 'password is too short')
            elif password != password2:
                messages.error(request, 'first password did not matched with another')
            else:
                First_name = first_name.capitalize()
                Last_name = last_name.capitalize()
                user = User.objects.create_user(
                        username=username, password=password2, first_name=First_name, last_name=Last_name, email=email)
                user.save()
                Buyer.objects.create(user = user , phone=phone, address=address)
                user = authenticate(username=username, password=password)
                login(request, user)
                return redirect('home')
            
    return render(request , 'register.html')


def logout_user(request):
    logout(request)
    return redirect('login')