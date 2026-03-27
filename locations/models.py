from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self) -> str:
        return self.name


class State(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name="states")
    name = models.CharField(max_length=100)

    class Meta:
        unique_together = ("country", "name")

    def __str__(self) -> str:
        return f"{self.name} ({self.country.name})"


class City(models.Model):
    state = models.ForeignKey(State, on_delete=models.CASCADE, related_name="cities")
    name = models.CharField(max_length=100)

    class Meta:
        unique_together = ("state", "name")

    def __str__(self) -> str:
        return f"{self.name} ({self.state.name})"

