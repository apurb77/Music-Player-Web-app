from django.shortcuts import render
from database.models import Arijit_Song

# Create your views here.

from django.http import HttpResponse
def home(request):
    # return HttpResponse("This is playlists  module")
    song = Arijit_Song.objects.all()
    return render(request,'arijitSongs.html',{'song':song})

def songpost(request,id):
    song =Arijit_Song.objects.filter(song_name=id).first()
    return render(request,songpost.html,{'song':song})

