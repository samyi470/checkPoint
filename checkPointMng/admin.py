from django.contrib import admin
from .models import MainMenu

from .models import AirportThroughput
from .models import TerminalThroughput
from .models import Airport
from .models import Terminal
from .models import Throughput


admin.site.register(AirportThroughput)
admin.site.register(TerminalThroughput)
admin.site.register(Airport)
admin.site.register(Terminal)
admin.site.register(Throughput)
admin.site.register(MainMenu)
