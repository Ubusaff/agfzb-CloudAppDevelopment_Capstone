from django.contrib import admin
from .models import CarMake, CarModel

#CarModelInline class
class CarModelInline(admin.TabularInline):
    model = CarModel

#CarModelAdmin class
class CarModelAdmin(admin.ModelAdmin):
    pass

#CarMakeAdmin class with CarModelInline
class CarMakeAdmin(admin.ModelAdmin):
    inlines = [CarModelInline]

#Register models here
admin.site.register(CarMake, CarMakeAdmin)
admin.site.register(CarModel, CarModelAdmin)