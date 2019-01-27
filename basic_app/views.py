from django.shortcuts import render
from basic_app.forms import UserForm,ProfileForm

from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse

def home(request):
    return render(request, 'home.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))
@login_required
def special(request):
    return HttpResponse('Welcome! You are logged in')

def user_login(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username= username, password = password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('home'))
            else:
                return HttpResponse("<h1> Your accoumt is not active </h1>")
        else:
            print(f'You have entered username ={username} and password = {password}')
            return HttpResponse('<h1>You have entered wrong username or password</h1>')

    else:
        return render(request, 'basic_app/login.html', {})



def register(request):

    registered = False
    if request.method == 'POST':

        user_form = UserForm(data = request.POST)
        profile_form = ProfileForm(data = request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit = False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                print('Found the picture')

                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True
        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = ProfileForm()

    return render(request, 'register.html',
                    {'user_form': user_form,
                    'profile_form': profile_form,
                    'registered': registered})
