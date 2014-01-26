from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.views.generic.base import TemplateView

from cdtracker.models import Album, Artist

def albumlist(request):
    """Displays a list of all our albums, sorted by the number of tracks on it."""
    context = {
        'albums': Album.objects.all().order_by('num_tracks')
    }
    return render_to_response('cdtracker/albumlist.html', context)


def album(request, album_id):
    """Displays info about a particular album"""
    context = {
        'album': Album.objects.get(id=album_id)
    }
    return render_to_response('cdtracker/album.html', context)


def artistlist(request):
    """Displays a list of all the artists that we know about"""
    pass
