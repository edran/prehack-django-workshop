from django.http import HttpResponse
from django.shortcuts import render

from cdtracker.models import Album, Artist

def albums(request):
    
    albums_list = str.join("", [ "<li>" + album.name + "</li>" for album in Album.objects.all() ] )
    
    html = "<html><ul>" + albums_list + "</ul></html>"
    
    return HttpResponse(html)


def artists(request):
    pass

def album(request, album_id):
    pass
