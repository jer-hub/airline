from django.shortcuts import render
from .models import Flight
from .forms import FlightForm
from django.urls import reverse
from django.http import HttpResponseRedirect

# Create your views here.
def index(request):
    flights = Flight.objects.all()
    form = FlightForm()
    return render(request, "flight/index.html", {
        "flights": flights,
        "forms": form,
    })

def add_flight(request):
    form = FlightForm(request.POST or None)
    if form.is_valid():
        form.save()
    return HttpResponseRedirect(reverse("flight:index"))

def delete_flight(request, id):
    flight = Flight.objects.get(id=id)
    flight.delete()
    return HttpResponseRedirect(reverse("flight:index"))

def update_flight(request, id):
    flight = Flight.objects.get(id=id)
    form = FlightForm(request.POST or None, instance=flight)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("flight:index")) 

    return render(request, "flight/update_view.html",{
        "forms": form,
        "pk": id
    })



