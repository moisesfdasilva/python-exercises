from django.http import Http404
from django.shortcuts import render, get_object_or_404
from events.models import Event


def event_details(request, event_id):
    try:
        event = get_object_or_404(Event, id=event_id)
        return render(request, 'details.html', {'event': event})
    except Http404:
        return render(request, '404.html')
