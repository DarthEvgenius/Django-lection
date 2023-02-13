from django.contrib import admin
# admin username = eugene, pass = 0000

from .models import Flight, Airport, Passenger

# Register your models here.

# Here we specify the admin view of Flight table
class FlightAdmin(admin.ModelAdmin):
	list_display = ("id", "origin", "destination", "duration")

# Adding horisintal filter for a Passenger to be able to register for a Flight
class PassengerAdmin(admin.ModelAdmin):
	# Here again we need a list of tuple for filter, so we have <,> at the end
	filter_horizontal = ("flights",)

admin.site.register(Airport)
# Here we give to the register not only Flight, but also the specified admin view
admin.site.register(Flight, FlightAdmin)
admin.site.register(Passenger, PassengerAdmin)