from django.conf.urls import url

from test_mlj import views

urlpatterns = [
               url(r'^$', views.index, name='index'),
               url(r'^album$', views.album, name='album'),
               url(r'^artist$', views.artist, name='artist'),
               url(r'^playlist$', views.playlist, name='playlist'),
               url(r'^track$', views.track, name='track'),
]
