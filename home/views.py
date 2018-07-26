from django.shortcuts import render, redirect, render_to_response
from django.contrib.auth.forms import UserCreationForm
from django.template.context_processors import csrf
from django.contrib import auth

def index(request):
    return render(request, 'home/homepage.html')

def register(request):
    args = {}
    args.update(csrf(request))
    args['form'] = UserCreationForm()
    if request.POST:
        newuser_form = UserCreationForm(request.POST)
        if newuser_form.is_valid():
            newuser_form.save()
            newuser = auth.authenticate(username = newuser_form.cleaned_data['username'], password=newuser_form.cleaned_data['password2'])
            auth.login(request, newuser)
            return redirect('/')
        else:
            args['form'] = newuser_form
    return render_to_response('home/register.html', args)