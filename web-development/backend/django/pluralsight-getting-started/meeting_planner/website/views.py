from django.shortcuts import render
from django.http import HttpResponse

from datetime import datetime


def index(request):
    return render(request, "website/index.html", context={'message': 'This a simple message to fill up as a template variable.'})


def about(request):
    return HttpResponse(f"Hi, this page have been devoloped by Andrés Castañeda.\n It is {datetime.now()}")