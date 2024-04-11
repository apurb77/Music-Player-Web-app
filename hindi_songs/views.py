from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
def hindi(request):
    # return HttpResponse("This is playlists  module")
    return render(request,'indexh.html')




