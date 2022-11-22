from django.shortcuts import render

from .models import Meeting


def get_meeting(pk):
    return Meeting.objects.get(pk=pk)


def detail(request, pk):
    meeting = get_meeting(pk)
    return render(request, 'meetings/detail.html', context={'meeting': meeting})
    