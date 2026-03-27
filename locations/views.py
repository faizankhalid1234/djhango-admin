from django.shortcuts import render

from .models import City, Country, State


def location_dropdown(request):
    """
    Chained dropdown without AJAX:
    - Uses GET parameters (country, state) and re-renders the page.
    - When country changes, form submits and server returns filtered states.
    - When state changes, form submits and server returns filtered cities.
    """

    countries = Country.objects.order_by("name")

    country_id = request.GET.get("country", "")
    state_id = request.GET.get("state", "")

    states = State.objects.none()
    cities = City.objects.none()

    selected_country = None
    selected_state = None

    if country_id:
        selected_country = Country.objects.filter(pk=country_id).first()
        if selected_country:
            states = selected_country.states.all().order_by("name")

    if state_id:
        selected_state = State.objects.filter(pk=state_id).first()
        if selected_state:
            cities = selected_state.cities.all().order_by("name")

    return render(
        request,
        "locations/location_dropdown.html",
        {
            "countries": countries,
            "states": states,
            "cities": cities,
            "country_id": str(country_id),
            "state_id": str(state_id),
            "selected_country": selected_country,
            "selected_state": selected_state,
        },
    )

