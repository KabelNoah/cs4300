from django.shortcuts import render, get_object_or_404, redirect
from rest_framework import viewsets
from django.http import HttpResponse
from .models import Movie, Seat, Booking
from .serializers import MovieSerializer, SeatSerializer, BookingSerializer

# Movie list view
def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'bookings/movieList.html', {'movies': movies}) 


def seat_booking(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    seats = Seat.objects.filter(movie=movie, is_booked=False)

    if request.method == "POST":
        seat_id = request.POST.get("seat")
        seat = get_object_or_404(Seat, id=seat_id)

        if seat.is_booked:
            return render(request, 'bookings/seatBooking.html', {
                'movie': movie, 'seats': seats, 'error': "Seat already booked."
            })

        Booking.objects.create(movie=movie, seat=seat)
        seat.is_booked = True
        seat.save()

        # Fix: Ensure only one `/proxy/3000/` in the redirect
        return redirect('/booking_history/')

    return render(request, 'bookings/seatBooking.html', {'movie': movie, 'seats': seats})


# Booking history view
def booking_history(request):
    bookings = Booking.objects.all()  # Get all bookings
    return render(request, 'bookings/bookingHistory.html', {'bookings': bookings})


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class SeatViewSet(viewsets.ModelViewSet):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

# Create your views here.
