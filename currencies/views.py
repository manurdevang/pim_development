from django.shortcuts import render
from django.shortcuts import redirect
# Create your views here.

def index(request):
    if request.user.is_authenticated:
        return render(request, 'currencies/index.html')
    else:
        return redirect("/accounts/login",foo='bar')

def new(request):
    if request.user.is_authenticated:
        return render(request, 'new.html', {'form': 'aaa'})
    else:
        return redirect("/accounts/login", foo='bar')

def create():
    return "{}"

def edit():
    return "{}"

def update():
    return "{}"

def destroy():
    return "{}"