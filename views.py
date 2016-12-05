from django.shortcuts import render
from django.http import HttpResponse

from test_mlj.models import Song
import spotipy


def index(request):
    context = {'list_of_songs': list_of_songs, 'length': len(list_of_songs)}
    return render(request, 'test_mlj/index.html', context)

def album(request):
    result = querySpotify(request.GET.get('q', ''), 'album')
    return render(request, 'test_mlj/index.html', result)

def artist(request):
    result = querySpotify(request.GET.get('q', ''), 'artist')
    return render(request, 'test_mlj/index.html', result)

def playlist(request):
    result = querySpotify(request.GET.get('q', ''), 'playlist')
    return render(request, 'test_mlj/index.html', result)

def track(request):
    result = querySpotify(request.GET.get('q', ''), 'track')
    return render(request, 'test_mlj/index.html', result)

def querySpotify(query, type):
    sp = spotipy.Spotify()
    search_result = sp.search(q=query, type=type)
    
    context = {'list_of_songs': search_result[type + 's']['items'], 'length': search_result[type + 's']['total'], 'result': search_result}
    return context
