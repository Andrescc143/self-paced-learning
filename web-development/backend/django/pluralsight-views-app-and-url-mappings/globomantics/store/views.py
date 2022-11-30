from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return HttpResponse("This is an e-commerce store. Here its home page.")