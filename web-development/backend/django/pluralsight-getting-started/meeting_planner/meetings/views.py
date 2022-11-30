from django.shortcuts import render, get_object_or_404, redirect

from django.forms import modelform_factory

from .models import Meeting, Room


def get_meeting(pk):
    return get_object_or_404(Meeting, pk=pk)


def detail(request, pk):
    meeting = get_meeting(pk)
    return render(request, 'meetings/detail.html', context={'meeting': meeting})


def rooms(request):
    rooms = Room.objects.all()
    return render(request, 'meetings/rooms.html', context={'rooms':rooms})


MeetingForm = modelform_factory(Meeting, exclude=[])


def new(request):    
    if request.method == 'POST':
        form = MeetingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = MeetingForm()
    return render(request, 'meetings/new.html', context={'form': form})