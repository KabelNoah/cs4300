from django.db import models
from django.contrib.auth.models import User

class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    release_date = models.DateField()
    duration = models.PositiveIntegerField() 

    def __str__(self):
        return self.title

def get_default_movie():
    movie = Movie.objects.first()
    return movie.id if movie else None 

class Seat(models.Model):
    movie = models.ForeignKey("Movie", on_delete=models.CASCADE, default=get_default_movie, null=True, blank=True)
    seat_number = models.CharField(max_length=10)
    is_booked = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.seat_number} for {self.movie.title}"



class Booking(models.Model):
    movie = models.ForeignKey("Movie", on_delete=models.CASCADE)
    seat = models.OneToOneField("Seat", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)  
    booking_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} booked {self.seat.seat_number} for {self.movie.title}"