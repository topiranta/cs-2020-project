from django.shortcuts import render, redirect
from django.http import HttpResponse
import sqlite3
from django.template import loader

def index(request):
    if 'owner' not in request.session:

        return render(request, 'notes/adduser.html')

    owner = request.session['owner']
    return render(request, 'notes/index.html', {'owner' : owner})

def addUser(request):

    owner = request.POST.get('owner')
    request.session['owner'] = owner

    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO notes_owner (nickname) VALUES (\'" + owner + "\')")
    conn.commit()

    return redirect('/notes/')

def badSessionRequest(request):
    return HttpResponse("Session list will be displayed here")

def note(request):
    

    return redirect('/notes/')
