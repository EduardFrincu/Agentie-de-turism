from django.contrib import admin
from .models import Client, Pachet_Turistic, Destinatie,Hotel,Transport,Responsabil, Plecare

# Register your models here.
admin.site.register(Client)
admin.site.register(Pachet_Turistic)
admin.site.register(Destinatie)
admin.site.register(Hotel)
admin.site.register(Transport)
admin.site.register(Responsabil)
admin.site.register(Plecare)

