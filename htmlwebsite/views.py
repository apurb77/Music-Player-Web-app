from django.shortcuts import render
# Create your views here.

from django.http import HttpResponse
def home(request):
    # return HttpResponse("This is HTML Website")
    return render(request,'index.html')

