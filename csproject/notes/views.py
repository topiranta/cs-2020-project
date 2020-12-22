from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Your notes will be displayed here")
