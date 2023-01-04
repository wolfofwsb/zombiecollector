from django.contrib import admin
# import your models here

from .models import Zombie, Feeding, Wound


# Register your models here
admin.site.register(Zombie)
admin.site.register(Feeding)
admin.site.register(Wound)