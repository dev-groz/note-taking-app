from django.shortcuts import render, redirect
from django.http import HttpResponse
from notes.models import Note

# Create your views here.
def all_notes(req):
    notes_list = Note.objects.all()
    return render(req, 'allnotes.html', {'notes_list': notes_list})

def get_note(req, note_id):
    note = Note.objects.get(id=note_id)
    return render(req, 'singlenote.html', {'note': note})

def create_note(req):
    if req.method == 'POST':
        header = req.POST.get('note-header')
        text = req.POST.get('note-text')
        return HttpResponse(header + " " + text)
    return redirect('/')
