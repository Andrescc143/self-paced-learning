from django.core.paginator import Paginator

from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return HttpResponse("This is an e-commerce store. Here its home page.")


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
    