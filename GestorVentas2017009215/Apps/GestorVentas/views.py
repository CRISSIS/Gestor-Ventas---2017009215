from django.shortcuts import render

# Create your views here.

def vistaIndex(request):
    return render(request, "index.html")