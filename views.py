from django.shortcuts import render, redirect
from django.http import HttpResponse

from test_mlj.models import Song
import spotipy


def index(request):
    return redirect('track')

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
    if query == '':
        context = {'items': [], 'length': 0, 'query': ''}
        return context
    else:
        sp = spotipy.Spotify()
        search_result = sp.search(q=query, type=type)
        context = {'items': search_result[type + 's']['items'], 'length': search_result[type + 's']['total'], 'query': query}
        return context
