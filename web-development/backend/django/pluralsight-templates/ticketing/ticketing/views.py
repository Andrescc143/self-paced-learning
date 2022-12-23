from django.http import HttpResponse
from django.shortcuts import render

from ticketing.models import Ticket


def index(request):
    return render(request, 'index.html')


def submit(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        body = request.POST.get('body')
        ticket = Ticket(submitter=username, body=body)
        ticket.save()
        return HttpResponse("The ticket has been saved succesfully!")
    return render(request, 'submit.html')


def tickets(request):
    tickets = Ticket.objects.all()
    return render(request, 'tickets.html', context={'tickets': tickets})