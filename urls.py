from django.conf.urls import url

from test_mlj import views

urlpatterns = [
               url(r'^$', views.index, name='index'),
]
