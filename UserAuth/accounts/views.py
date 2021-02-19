from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth

def login(requests):
    if requests.method == 'POST':
        username = requests.POST['username']
        password = requests.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(requests, user)
            return redirect('/')
        else:
            messages.info(requests, 'invalid username or password')
            return render(requests, 'login.html')
    else:
        return render(requests, 'login.html')


def logout(requests):
    auth.logout(requests)
    messages.info(requests, 'successfully! logged out')
    return redirect('/')


def register(requests):
    if requests.method == 'POST':
        first_name = requests.POST['first_name']
        last_name = requests.POST['last_name']
        email = requests.POST['email']
        photo = requests.POST['photo']
        username = requests.POST['username']
        password1 = requests.POST['password1']
        password2 = requests.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(requests, 'Username taken')
                print('Username taken')
                return render(requests, 'register.html')
            elif User.objects.filter(email=email).exists():
                messages.info(requests, 'email taken')
                print('email taken')
                return render(requests, 'register.html')
            else:
                user = User.objects.create_user(
                    username=username, password=password1, first_name=first_name, last_name=last_name, email=email)
                user.save()
                print('user created')
                return redirect('login')
        else:
            messages.info(requests, 'Passwords not matching')
            print('Passwords not matching')
            return render(requests, 'register.html')
    else:
        return render(requests, 'register.html')
