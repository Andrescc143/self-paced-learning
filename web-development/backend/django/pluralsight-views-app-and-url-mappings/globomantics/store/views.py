from django.core.paginator import Paginator
from django.views import View

from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    response = render(request, 'store/index.html')
    if request.COOKIES.get('visits'):
        value = int(request.COOKIES.get('visits'))
        print('Getting cookie...')
        response.set_cookie('visits', value + 1)
    else:
        response.set_cookie('visits', 1)
    return response
    

def detail(request):
    return HttpResponse('This is the detail webpage.')


def electronics(request):
    items = ['Windows PC', 'MAC', 'iPhone', 'Samsung A71', 'Macbook Pro 14"', 'PS4', 'XBOX']
    if request.method == 'GET':
        paginator = Paginator(items, 2)
        pages = request.GET.get('page', 1)
        try:
            items = paginator.page(pages)
        except PageNotAnInteger:
            items = paginator.page(1)
        return render(request, 'store/list.html', context={'items': items})
    else:
        HttpResponse(f'{request.method} Method not allowed.')


class ElectronicsView(View):
    def get(self, request):
        items = ('Windows PC', 'MAC', 'iPhone', 'Samsung A71', 'Macbook Pro 14"', 'PS4', 'XBOX')
        paginator = Paginator(items, 2)
        pages = request.GET.get('page', 1)
        try:
            items = paginator.page(pages)
        except PageNotAnInteger:
            items = paginator.page(1)
        return render(request, 'store/list.html', context={'items': items})
        