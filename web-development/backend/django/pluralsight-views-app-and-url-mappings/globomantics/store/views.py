from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return HttpResponse("This is an e-commerce store. Here its home page.")


def detail(request):
    return HttpResponse('This is the detail webpage.')


def electronics(request):
    return HttpResponse('This is the electronics webpage.')