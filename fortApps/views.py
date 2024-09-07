from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import DataCentre

# Create your views here.



def index(request):
    data = DataCentre.objects.all()
    return render(request, "fortApps/index.html", {"data" : data})

def form(request):
    if request.method == 'POST':
        dta =  request.POST
        name = dta.get("name")
        status = dta.get("status")
        color = dta.get("color")
        wt = dta.get("wt")
        DataCentre.objects.create(name=name, status=status, color=color, wt=wt)
        return redirect("/")
    return render(request, "fortApps/form.html")

def edit(request, pk):
    if request.method == 'POST':
        dtx = request.POST
        name = dtx.get("name")
        status = dtx.get("status")
        color = dtx.get("color")
        wt = dtx.get("wt")
        stx = DataCentre.objects.get(id=pk)
        stx.name = name
        stx.status = status
        stx.color = color
        stx.wt = wt
        stx.save()
        return redirect('/')
    dets = DataCentre.objects.get(id=pk)
    return render(request, "fortApps/edit.html", {'dets' : dets})

def delete(request, pk):
    DataCentre.objects.get(id=pk).delete()
    return redirect('/')






