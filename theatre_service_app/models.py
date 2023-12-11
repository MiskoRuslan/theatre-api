from django.conf import settings
from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name


class Actor(models.Model):
    first_name = models.CharField(max_length=63)
    last_name = models.CharField(max_length=63)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Play(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    actors = models.ManyToManyField(Actor, related_name="plays")
    genres = models.ManyToManyField(Genre, related_name="plays")

    def __str__(self) -> str:
        return self.title


class Reservation(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )

    def __str__(self):
        return str(self.created_at)

    class Meta:
        ordering = ["-created_at"]


class TheatreHall(models.Model):
    name = models.CharField(max_length=255)
    rows = models.IntegerField()
    seats_in_row = models.IntegerField()

    def __str__(self) -> str:
        return self.name


class Performance(models.Model):
    play = models.ForeignKey(Play, on_delete=models.CASCADE)
    theatre_hall = models.ForeignKey(TheatreHall, on_delete=models.CASCADE)
    show_time = models.DateTimeField()

    def __str__(self) -> str:
        return (f"Show time: {self.show_time}\n"
                f"Play: {self.play.title}\n"
                f"Theatre hall: {self.theatre_hall.name}")


class Ticket(models.Model):
    row = models.IntegerField()
    seat = models.IntegerField()

    performance = models.ForeignKey(Performance,
                                    on_delete=models.SET_NULL,
                                    null=True, blank=True,
                                    related_name="tickets")

    reservation = models.ForeignKey(Reservation,
                                    on_delete=models.SET_NULL,
                                    null=True, blank=True,
                                    related_name="tickets")

    def __str__(self) -> str:
        return (f"Reservation Time: {self.reservation.created_at}\n"
                f"Performance: {self.performance.play.title}\n"
                f"Theatre Hall: {self.performance.theatre_hall.name}\n"
                f"Row #{self.row}, Seat #{self.seat}")

