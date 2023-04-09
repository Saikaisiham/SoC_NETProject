from django.shortcuts import render
from User_Profile.models import perPage

# Create your views here.

def index(request):
    test = perPage.objects.all
    context = {
        'test' : test
    }
    return render(request, 'index.html',context)