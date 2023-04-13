from django.test import TestCase, Client
from django.db.models import Max

from .models import Airport, Flight, Passenger

# Create your tests here.
class FlightTestCase(TestCase):
    
	# Initial setup, creating testing database
	def setUp(self):

		# Create airports
		a1 = Airport.objects.create(code="AAA", city="City A")
		a2 = Airport.objects.create(code="BBB", city="City B")

		# Create flights
		Flight.objects.create(origin=a1, destination=a2, duration=100)
		Flight.objects.create(origin=a1, destination=a1, duration=200)
		Flight.objects.create(origin=a1, destination=a2, duration=-100)

	def test_departures_count(self):
		a = Airport.objects.get(code="AAA")
		# 'deparures' mistake in models name
		self.assertEqual(a.deparures.count(), 3)

	def test_arrivals_count(self):
		a = Airport.objects.get(code="AAA")
		self.assertEqual(a.arrivals.count(), 1)

	def test_valid_flight(self):
		a1 = Airport.objects.get(code="AAA")
		a2 = Airport.objects.get(code="BBB")
		f = Flight.objects.get(origin=a1, destination=a2, duration=100)
		self.assertTrue(f.is_valid_flight())

	def test_invalid_flight_destination(self):
		a1 = Airport.objects.get(code="AAA")
		f = Flight.objects.get(origin=a1, destination=a1)
		self.assertFalse(f.is_valid_flight())

	def test_invalid_flight_duration(self):
		a1 = Airport.objects.get(code="AAA")
		a2 = Airport.objects.get(code="BBB")
		f = Flight.objects.get(origin=a1, destination=a2, duration=-100)
		self.assertFalse(f.is_valid_flight())

	# Now testing GET requests for pages, imitating client's requests to the server
	def test_index(self):
		# Create "user"
		c = Client()
		# Imitate user's response to the main page of app
		# Everything that server will get back will be saved in the variable
		response = c.get("/flights/")
		# Check that status code will be OK
		self.assertEqual(response.status_code, 200)
		# Access the context of request, make sure it contents what it should content
		# In our case there must be key "flights" and 3 values in it
		self.assertEqual(response.context["flights"].count(), 3)

	def test_valid_flight_page(self):
		a1 = Airport.objects.get(code="AAA")
		# This isn't a valid flight, but it should be on a page, as it exists in db
		f = Flight.objects.get(origin=a1, destination=a1)

		c = Client()
		# Response that flight page
		response = c.get(f"/flights/{f.id}")
		self.assertEqual(response.status_code, 200)

	def test_invalid_flight_page(self):
		# Get maximum value of id's in db
		# ["id__max"] returns the maximum possible value of id
		max_id = Flight.objects.all().aggregate(Max("id"))["id__max"]

		c = Client()
		# Trying to get flight that not exists
		response = c.get(f"/flights/{max_id+1}")
		# There must not be such a page
		self.assertEqual(response.status_code, 404)

	def test_flight_page_passengers(self):
		# get a flight
		f = Flight.objects.get(pk=1)
		# Create a passenger
		p = Passenger.objects.create(first="Alice", last="Adams")
		# Add passenger to flight
		f.passengers.add(p)

		c = Client()
		# Make a request for flight's page
		response = c.get(f"/flights/{f.id}")
		# Check status code
		self.assertEqual(response.status_code, 200)
		# Check context with key "passengers"
		self.assertEqual(response.context["passengers"].count(), 1)

	def test_flight_page_non_passengers(self):
		f = Flight.objects.get(pk=1)
		p = Passenger.objects.create(first="Alice", last="Adams")

		c = Client()
		response = c.get(f"/flights/{f.id}")
		self.assertEqual(response.status_code, 200)
		self.assertEqual(response.context["non_passengers"].count(), 1)