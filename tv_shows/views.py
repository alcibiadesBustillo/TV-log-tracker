import time
import datetime 
from django.shortcuts import render, redirect

# Create your views here.
from .models import Show, Spent
from .forms import ShowForm

from .auxiliar import td_format


def home(request):
    shows = Show.objects.all()
    #print(shows.values())
    context = {'shows': shows}
    return render(request,'tv_shows/index.html', context)

def show(request, pk):
    spents = Spent.objects.filter(show=pk)
    total_time = ''
    tv_show = ''
    try:
        total_time = datetime.timedelta(0,0,0,0,0,0)
        for s in spents:
            date = datetime.date(1, 1, 1)
            datetime1 = datetime.datetime.combine(date, s.initial_time)
            datetime2 = datetime.datetime.combine(date, s.final_time)
            total_time += datetime2 - datetime1
        total_time = td_format(total_time)
        tv_show = spents[0].show.name
    except Exception:
        pass           
    
    #print(total_time)

    #print(spents.values())    
    context = {
        'spents': spents,
        'tv_show': tv_show,
        'total_time_elapse':  total_time}   
    return render(request, 'tv_shows/show.html', context)

def createShow(request):
    form = ShowForm()
    
    if request.method == 'POST':
        form = ShowForm(request.POST)
        if form.is_valid():
            show = Show.objects.create(
                name = form.cleaned_data['name'],
                author = request.user,                     
            )
            show.categories.set(form.cleaned_data['categories'])
        return redirect('index')

    context = {'form': form}   
    return render(request, 'tv_shows/show_form.html', context)