from django.contrib import admin

# Register your models here.

from exames.models import Exames
admin.site.register(Exames)

#acrescentamos a nossa classe Exames nos registros do admin