from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
import sqlite3
import json
from django.views.decorators.csrf import csrf_exempt

def index(request):
    if 'owner' not in request.session:

        return render(request, 'notes/adduser.html')

    owner = request.session['owner']
    birthYear = request.session['birthYear']
    return render(request, 'notes/index.html', {'owner' : owner, 'birthYear' : birthYear})

def addUser(request):

    owner = request.POST.get('owner')
    birthYear = request.POST.get('birthYear')
    request.session['owner'] = owner
    request.session['birthYear'] = birthYear

    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO notes_owner (nickname) VALUES (\'" + owner + "\')")
    conn.commit()
    conn.close()

    return redirect('/notes/')

def error(request):
    return HttpResponse("errr")

@csrf_exempt
def note(request):

    notes = []
    owners = []
    sessionOwner = ''

    if request.method == 'GET':
        sessionOwner = request.GET.get('owner')
    elif request.method == 'POST':
        sessionOwner = request.POST.get('owner')

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

        conn.close()
        return HttpResponse('Owner not in list of owners ' + str(owners))


    if request.method == 'GET':


        for row in cursor.execute("SELECT note_text FROM notes_note WHERE owner_id =\'" + ownerId + "\'"):

            strng = str(row).replace("'", "")
            strng = strng.replace(",", "")
            strng = strng.replace("(", "")
            strng = strng.replace(")", "")
            print(strng)
            notes.append(strng)

        conn.close()
        return HttpResponse(json.dumps(notes) + "<br> <br> <a href=\"/notes\">To front page</a>")

    if request.method == 'POST':

        text = str(request.POST.get('text'))
        cursor.execute("INSERT INTO notes_note (owner_id, note_text) VALUES (\'" + ownerId + "\', \'" + text + "\')")
        conn.commit()


        conn.close()
        return redirect('/notes/')




    conn.close()
    return redirect('/notes/')
