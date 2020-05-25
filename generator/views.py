from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def home(request):
    return render(request,'generator/home.html')

def password(request):

    charachters = list('abcdefghijklmnopqrstuvwxyz')

    length = int(request.GET.get('length'))

    if request.GET.get('uppercase'):
        charachters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('numbers'):
        charachters.extend(list('01234564789'))

    if request.GET.get('special'):
        charachters.extend(list('!@#$%^&*()_+~<>?/'))

    thepassword = ''

    for i in range(length):
        thepassword += random.choice(charachters)

    return render(request,'generator/password.html',{'password':thepassword})

def about(request):
    return render(request,'generator/about.html')
