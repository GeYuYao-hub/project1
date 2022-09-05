from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("l am happy!!!!!!")

# Create your views here.
