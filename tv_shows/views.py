import time
import datetime 
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

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
        'total_time_elapse':  total_time,
        'pk1': pk
        }   
    return render(request, 'tv_shows/show.html', context)

@login_required(login_url="index")
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

@login_required(login_url="index")
def updateShow(request, pk):
    show = Show.objects.get(pk=pk)
    form = ShowForm(instance=show)    
    if request.method == 'POST':
        form = ShowForm(request.POST)
        if form.is_valid():
            show.name = form.cleaned_data['name']
            show.author = request.user 
            show.save()
            show.categories.set(form.cleaned_data['categories'])
        return redirect('index')
    context = {'form': form}   
    return render(request, 'tv_shows/show_form.html', context)

@login_required(login_url="index")
def deleteShow(request, pk):
    show = Show.objects.get(pk=pk)
    if request.method == 'POST':
        show.delete()
        return redirect('index')

    context = {'show': show}   
    return render(request, 'tv_shows/delete_show.html', context)
    
@login_required(login_url="index")    
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

@login_required(login_url="index")
def updateSpent(request, pk1, pk2):
    spent = Spent.objects.get(pk=pk2)
    form = SpentForm(instance=spent)      
    if request.method == 'POST':        
        form = SpentForm(request.POST)
        if form.is_valid():            
            s = Spent.objects.get(pk=pk2)
            s.show = get_object_or_404(Show, pk=pk1)
            s.date = form.cleaned_data['date']
            s.initial_time = form.cleaned_data['initial_time']
            s.final_time = form.cleaned_data['final_time']
            s.save()          
        return redirect('show', pk=pk1)
    context = {'form': form}   
    return render(request, 'tv_shows/spent_form.html', context)

@login_required(login_url="index")
def deleteSpent(request, pk1, pk2):
    spent = Spent.objects.get(pk=pk2)
    if request.method == 'POST':
        spent.delete()
        return redirect('show', pk=pk1)

    context = {'spent': spent}   
    return render(request, 'tv_shows/delete_spent.html', context)

