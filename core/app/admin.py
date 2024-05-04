from django.contrib import admin
from .models import Apartment, Client, Manager, ObjectName

admin.site.register(Apartment)
admin.site.register(Client)
admin.site.register(Manager)
admin.site.register(ObjectName)

