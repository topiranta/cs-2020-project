from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
import sqlite3
import json
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
    conn.close()

    return redirect('/notes/')

def error(request):
    return HttpResponse("errr")

def note(request):


    if request.method == 'GET':

        notes = []
        owners = []
        sessionOwner = request.GET.get('owner')
        ownerId = ''
        conn = sqlite3.connect('db.sqlite3')
        cursor = conn.cursor()

        for row in cursor.execute("SELECT id, nickname FROM notes_owner"):
            owners.append(row)
        print(owners)

        for o in owners:

            if o[1] == sessionOwner:

                ownerId = str(o[0])
                pass

        if ownerId == '':

            return HttpResponse('Owner not in list of owners ' + str(owners))


        for row in cursor.execute("SELECT note_text FROM notes_note WHERE owner_id =\'" + ownerId + "\'"):

            notes.append(row)

        return HttpResponse(json.dumps(notes))




    return redirect('/notes/')
