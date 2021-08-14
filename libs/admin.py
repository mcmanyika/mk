from django.contrib import admin
from .models import DeployedTickets

# tickects


class TicketsAdmin(admin.ModelAdmin):
    list_display = ('id', 'accountAddress')


admin.site.register(DeployedTickets, TicketsAdmin)
