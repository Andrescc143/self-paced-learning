from django.shortcuts import render
from django.http import HttpResponse

from datetime import datetime

from meetings.models import Meeting


def index(request):
    num_meeting = Meeting.objects.count()
    return render(request, "website/index.html", context={'num_meeting': num_meeting})


def about(request):
    return HttpResponse(f"Hi, this page have been devoloped by Andrés Castañeda.\n It is {datetime.now()}")