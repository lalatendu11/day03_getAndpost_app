from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def getInput(request):
    return render(request, template_name="getinput.html")


def postInput(request):
    return render(request, template_name="postinput.html")


def add(request):
    if request.method == "POST":
        x = request.POST["t1"]
        y = request.POST["t2"]
        i = int(x)
        j = int(y)
        k = i + j
        return HttpResponse("<html><h2>The sum is:</h2></html>" + str(k))
    else:
        x = request.GET["t1"]
        y = request.GET["t2"]
        i = int(x)
        j = int(y)
        k = i + j
        return HttpResponse("<html><h2>The sum is:</h2></html>" + str(k))
