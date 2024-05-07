from django.contrib import admin
from flight.models import Airport, Flight, Passenger
# Register your models here.

admin.site.register(Airport)
admin.site.register(Flight)
admin.site.register(Passenger)