import time
import datetime 
from django.shortcuts import render

# Create your views here.
from .models import Show, Spent
from .auxiliar import td_format


def home(request):
    shows = Show.objects.all()
    #print(shows.values())
    context = {'shows': shows}
    return render(request,'tv_shows/index.html', context)

def show(request, pk):
    spents = Spent.objects.filter(show=pk)    
    total_time = datetime.timedelta(0,0,0,0,0,0)
    for s in spents:
        date = datetime.date(1, 1, 1)
        datetime1 = datetime.datetime.combine(date, s.initial_time)
        datetime2 = datetime.datetime.combine(date, s.final_time)
        total_time += datetime2 - datetime1
    #print(total_time)

    #print(spents.values())    
    context = {
        'spents': spents,
        'tv_show': spents[0].show.name,
        'total_time_elapse': td_format(total_time) }   
    return render(request, 'tv_shows/show.html', context)