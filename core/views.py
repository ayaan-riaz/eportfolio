from django.shortcuts import render
from django.http import HttpResponse
import datetime

def hellotime(request):
    now = datetime.datetime.now()
    return HttpResponse(f"<h1>Hello, world!</h3> <p>It's {now}.</h3>")

def screenprint(request):
    return render(request, "core/screenprint.html")

def blackbox(request):
    return render(request, "core/blackbox.html")