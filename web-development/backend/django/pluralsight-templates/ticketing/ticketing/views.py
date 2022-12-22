from django.http import HttpResponse
from django.shortcuts import render

from ticketing.models import Ticket


def index(request):
    return render(request, 'index.html')


def submit(request):
    ticket = Ticket(submitter='Test_user', body="This is a ticket to use as an example.")
    ticket.save()
    print("Ticket saved correctly")
    return render(request, 'submit.html')


def tickets(request):
    tickets = Ticket.objects.all()
    return render(request, 'tickets.html', context={'tickets': tickets})