
from django.http import HttpResponse
from .models import CalendarEv

# Create your views here.

def calendar_view(request):
    calendar_ev = CalendarEv()
    calendar_ev.date
    HttpResponse('it worked')