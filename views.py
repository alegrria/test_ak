from django.shortcuts import render
from django.http import HttpResponse

from test_mlj.models import Song
import spotipy


def index(request):
    song1 = Song('song1', 'pic1')
    song2 = Song('song2', 'pic2')
    list_of_songs = []
    list_of_songs.append(song1)
    list_of_songs.append(song2)

    context = {'list_of_songs': list_of_songs, 'length': len(list_of_songs)}
    return render(request, 'test_mlj/index.html', context)

def album(request):
    song1 = Song('song1', 'pic1')
    song2 = Song('song2', 'pic2')
    list_of_songs = []
    list_of_songs.append(song1)
    list_of_songs.append(song2)
    result = querySpotify(request.GET.get('q', ''), 'album')
    context = {'list_of_songs': list_of_songs, 'length': len(list_of_songs), 'result': result}
    return render(request, 'test_mlj/index.html', context)

def artist(request):
    song1 = Song('song1', 'pic1')
    song2 = Song('song2', 'pic2')
    list_of_songs = []
    list_of_songs.append(song1)
    list_of_songs.append(song2)
    context = {'list_of_songs': list_of_songs, 'length': len(list_of_songs)}
    return render(request, 'test_mlj/index.html', context)

def playlist(request):
    song1 = Song('song1', 'pic1')
    song2 = Song('song2', 'pic2')
    list_of_songs = []
    list_of_songs.append(song1)
    list_of_songs.append(song2)
    context = {'list_of_songs': list_of_songs, 'length': len(list_of_songs)}
    return render(request, 'test_mlj/index.html', context)

def track(request):
    song1 = Song('song1', 'pic1')
    song2 = Song('song2', 'pic2')
    list_of_songs = []
    list_of_songs.append(song1)
    list_of_songs.append(song2)
    context = {'list_of_songs': list_of_songs, 'length': len(list_of_songs)}
    return render(request, 'test_mlj/index.html', context)

def querySpotify(query, type):
    sp = spotipy.Spotify()
    return sp.search(q=query, type=type)
