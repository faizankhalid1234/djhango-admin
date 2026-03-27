from django.contrib import admin

from .models import City, Country, State


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    list_display = ("id", "name")


@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    list_display = ("id", "name", "country")
    list_filter = ("country",)


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    list_display = ("id", "name", "state")
    list_filter = ("state",)

