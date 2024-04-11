from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def main(request):
    # return HttpResponse("This is playlists  module")
    return render(request,'arijitSongs.html')

