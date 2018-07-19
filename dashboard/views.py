from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
import os
from django.http import HttpResponseRedirect
#@login_required(login_url='/accounts/login/')


# Create your views here.
def index(request):
    if request.user.is_authenticated:
        return render(request,'dashboard/index.html',{})
    else:
        return redirect("/accounts/login",foo='bar')