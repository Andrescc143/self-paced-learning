from django.shortcuts import render
from django.http import HttpResponse

from datetime import datetime

from meetings.models import Meeting


def index(request):
    meetings = Meeting.objects.all()
    return render(request, "website/index.html", context={'meetings': meetings})


def about(request):
    return HttpResponse(f"Hi, this page have been devoloped by Andrés Castañeda.\n It is {datetime.now()}")