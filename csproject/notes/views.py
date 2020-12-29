from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader

def index(request):
    if 'owner' not in request.session:

        return redirect('/notes/user/')

#    return HttpResponse("Your notes will be displayed here")
    owner = request.session['owner']
    return render(request, 'notes/index.html', {'owner' : owner})

def addUser(request):

    request.session['owner'] = 'matti'

    return HttpResponse("You can enter your name here")

def badSessionRequest(request):
    return HttpResponse("Session list will be displayed here")

def addNote(request):
    return HttpResponse("You can add a note here")
