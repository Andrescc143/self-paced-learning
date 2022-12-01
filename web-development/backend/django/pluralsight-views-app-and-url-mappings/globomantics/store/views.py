from django.core.paginator import Paginator
from django.views import View
from django.http import HttpResponse

from django.shortcuts import render
from django.views.decorators.cache import cache_page


@cache_page(900)
def index(request):
    user_name = 'Andres'
    if not request.session.has_key('customer'):
        request.session['customer'] = user_name
        print('Session value set')
    response = render(request, 'store/index.html')
    if request.COOKIES.get('visits'):
        value = int(request.COOKIES.get('visits'))
        print('Getting cookie...')
        response.set_cookie('visits', value + 1)
    else:
        response.set_cookie('visits', 1)
    return response
    

def logout(request):
    try:
        del request.session['customer']
    except KeyError:
        print("Error while logging out")
    return HttpResponse("You're logged out.")


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
        