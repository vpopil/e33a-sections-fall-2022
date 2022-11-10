from django.contrib import admin


from .models import Make, Type, Vehicle

admin.site.register(Make)
admin.site.register(Type)
admin.site.register(Vehicle)