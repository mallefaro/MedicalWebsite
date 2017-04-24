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
        print(form.cleaned_data['email'])
    return render(request, 'lk/registration.html', locals())
def register(request):
    args = {}
    args.update(csrf(request))
    args['form'] = UserCreationForm()
    if request.POST:
        newUserForm = UserCreationForm(request.POST)
        if newUserForm.is_valid():
            newUserForm.form_save()
            newUser = auth.authenticate(username=newUserForm.cleaned_data['username'],
                                        password=newUserForm.cleaned_data['password2'])
            auth.login(request, newUser)
            return redirect('/')
        else:
            args['form'] = newUserForm
    return render_to_response('lk/registration.html', args)

