import time
import datetime 
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from .models import Show, Spent
from .forms import ShowForm, SpentForm

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

def createSpent(request, pk):
    form = SpentForm()#initial={'show': pk})
    #form.fields['show'].widget.attrs['readonly'] = True
    if request.method == 'POST':
        form = SpentForm(request.POST)        
        #print()
        if form.is_valid():
            #id = request.POST['show']
            Spent.objects.create(
                show = get_object_or_404(Show, pk=pk),
                date = form.cleaned_data['date'],
                initial_time = form.cleaned_data['initial_time'],
                final_time = form.cleaned_data['final_time'],
            )
            #form.save()
        return redirect('show', pk=pk)

    context = {'form': form}   
    return render(request, 'tv_shows/spent_form.html', context)

