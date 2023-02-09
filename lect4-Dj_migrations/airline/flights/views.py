from django.shortcuts import render

from .models import Flight

# Create your views here.
def index(request):
	""" Shows all the flihts """

	return render(request, "flights/index.html", {
		"flights": Flight.objects.all()
	})

def flight(request, flight_id):
	""" Shows info about a flight """

	# Get the flight, "pk" here is for "Primary Key" of the table, for id precisely
	flight = Flight.objects.get(pk=flight_id)

	# Render a template with this flight
	return render(request, "flights/flight.html", {
		"flight": flight
	})