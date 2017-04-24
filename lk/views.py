from django.shortcuts import render, render_to_response, redirect
from django.contrib import auth
from django.template.context_processors import csrf
from django.contrib.auth.forms import UserCreationForm
from userProfile.forms import userProfileForm
def lk(request):
   return render(request, 'lk/auth.html', locals())
def registration(request):
    form = userProfileForm(request.POST or None)
    if request.method == 'POST' and form .is_valid():
        form.save()
        return redirect('registration.html')
    return render(request, 'lk/registration.html', locals())

def logout(request):
    auth.logout(request)
    return redirect('/')
def login(request):
    args = {}
    args.update(csrf(request))
    if request.POST:
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(email=email, password=password)
        if user is not None:
            auth.login(request, user)
            print("you are loggined, boss")
            return redirect('/')
        else:
            args['login_error'] = "Пользователь не найден"
            return  render_to_response('lk/auth.html', args)
    else:
        return render_to_response('lk/auth.html', args)


