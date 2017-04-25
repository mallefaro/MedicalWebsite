from django.shortcuts import render, render_to_response, redirect
from django.contrib import auth as AUTH
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.template.context_processors import csrf
from django.contrib.auth.forms import UserCreationForm
from userProfile.forms import userProfileForm
def lk(request):
    form_auth = AuthenticationForm()
    return render(request, 'lk/auth.html', locals())

def auth(request):
    if request.user.is_authenticated():
        return redirect('/')
    elif request.method == 'POST':
        form_auth = AuthenticationForm(request=request, data=request.POST)
        if form_auth.is_valid():
            user = form_auth.get_user()
            AUTH.login(request, user)
            return redirect("/")
    else:
        form_auth = AuthenticationForm()
    return render(request, "lk/auth.html", {'form_auth': form_auth})

def registration(request):
    form = userProfileForm(request.POST or None)
    if request.method == 'POST' and form .is_valid():
        form.save()
        return redirect('registration.html')
    return render(request, 'lk/registration.html', locals())

def logout(request):
    AUTH.logout(request)
    return redirect('/')
