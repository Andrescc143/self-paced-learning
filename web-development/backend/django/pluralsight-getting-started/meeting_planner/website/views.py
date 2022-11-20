from django.shortcuts import render
from django.http import HttpResponse

from datetime import datetime


def index(request):
    return HttpResponse('Welcome to the main webpage for this application')


def about(request):
    return HttpResponse(f"Hi, this page have been devoloped by Andrés Castañeda.\n It is {datetime.now()}")