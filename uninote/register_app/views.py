from django.shortcuts import render
from register_app.forms import UserForm,UserProfileInfoForm

from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse

# Create your views here.

def homepage(request):
    return render(request,'register_app/homepage.html')

def about(request):
    return render(request,'register_app/about.html')

def discussions(request):
    return render(request,'register_app/discussions.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('homepage'))

def register(request):
    registered = False
    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user=user_form.save()
            # HASHING PASSWORD
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form= UserForm()
        profile_form = UserProfileInfoForm()
    return render(request, 'register_app/registration.html', {'user_form':user_form,'profile_form':profile_form,'registered':registered})


def user_login(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('homepage'))

            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")
        else:
            return HttpResponse("Invalid login details suplied")

    else:
        return render(request, 'register_app/login.html', {})
