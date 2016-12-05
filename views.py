from django.shortcuts import render
from django.http import HttpResponse

from test_mlj.models import Song

def index(request):
    song1 = Song('song1', 'pic1')
    song2 = Song('song2', 'pic2')
    list_of_songs = []
    list_of_songs.append(song1.name)
    list_of_songs.append(song2.name)
    return render(request, 'test_mlj/index.html', {})

