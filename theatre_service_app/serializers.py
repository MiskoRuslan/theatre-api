from django.db import transaction
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from theatre_service_app.models import Genre, Actor, TheatreHall


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ("id", "name")


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ("id", "first_name", "last_name", "full_name")


class TheatreHallSerializer(serializers.ModelSerializer):
    class Meta:
        model = TheatreHall
        fields = ("id", "name", "rows", "seats_in_row", "capacity")


class PlaySerializer():
    pass


class PlayListSerializer():
    pass


class PlayDetailSerializer():
    pass


class PlayImageSerializer():
    pass
