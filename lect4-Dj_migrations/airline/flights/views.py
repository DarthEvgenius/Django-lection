from django.shortcuts import render

from .models import Flight, Passenger

from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.

def index(request):
	""" Shows all the flihts """

	return render(request, "flights/index.html", {
		"flights": Flight.objects.all()
	})

def flight(request, flight_id):
	""" Shows info about a flight """
	# Need an error check for invalid flight_id

	# Get the flight, "pk" here is for "Primary Key" of the table, for id precisely
	flight = Flight.objects.get(pk=flight_id)

	# Render a template with this flight
	return render(request, "flights/flight.html", {
		"flight": flight,
		# A "flight" doesn't have a "passengers" list inside, but due to "related_name" in models "Passenger" we can get access to this list
		"passengers": flight.passengers.all(),
		# We exclude the people that are not passengers of this flight, passengers that don't have this flight in their list of flights
		"non_passengers": Passenger.objects.exclude(flights=flight).all()
	})


def book(request, flight_id):
	""" We can book flights for passengers """
	# Needs an error check for invalid flights or passengers

	# Via "GET" method ==> view the page, via "POST" ==> update database
	if request.method == "POST":
		# Get the flight
		flight = Flight.objects.get(pk=flight_id)
		# Get the passenger from the input name="passenger"
		passenger = Passenger.objects.get(pk=int(request.POST["passenger"]))
		# Add this flight to the passenger's list
		passenger.flights.add(flight)
		# Render a page, redirect
		# reverse takes a name of some view and finds out the url
		# Pay attention to args syntax: it's a tuple, so we have <,> at the end inside ()
		return HttpResponseRedirect(reverse("flight", args=(flight.id,)))