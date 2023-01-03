from django.contrib import admin
# import your models here

from .models import Zombie, Feeding
from .models import Zombie

# Register your models here
admin.site.register(Zombie)
admin.site.register(Feeding)