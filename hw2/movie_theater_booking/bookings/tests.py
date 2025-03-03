from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from .models import Movie, Seat, Booking

class MovieModelTest(TestCase):
    def setUp(self):
        self.movie = Movie.objects.create(
            title="Django Unchained",
            description="A bounty hunter frees a slave and they take down a plantation owner.",
            release_date="2012-12-25",
            duration=165
        )

    def test_movie_creation(self):
        self.assertEqual(self.movie.title, "Django Unchained")
        self.assertEqual(self.movie.description, "A bounty hunter frees a slave and they take down a plantation owner.")
        self.assertEqual(self.movie.duration, 165)

class SeatModelTest(TestCase):
    def setUp(self):
        self.seat = Seat.objects.create(seat_number="A1", is_booked=False)

    def test_seat_creation(self):
        self.assertEqual(self.seat.seat_number, "A1")
        self.assertFalse(self.seat.is_booked)

class BookingModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username="testuser")
        self.movie = Movie.objects.create(
            title="Django Unchained",
            description="A bounty hunter frees a slave and they take down a plantation owner.",
            release_date="2012-12-25",
            duration=165
        )
        self.seat = Seat.objects.create(seat_number="B2", is_booked=False)

    def test_booking_creation(self):
        booking = Booking.objects.create(
            user=self.user, movie=self.movie, seat=self.seat
        )
        self.assertEqual(booking.user.username, "testuser")
        self.assertEqual(booking.movie.title, "Django Unchained")
        self.assertEqual(booking.seat.seat_number, "B2")

class APITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username="testuser", password="password")

        # Create test movie
        self.movie = Movie.objects.create(
            title="Django Unchained",
            description="A bounty hunter frees a slave and they take down a plantation owner.",
            release_date="2012-12-25",
            duration=165
        )

        # Create test seat
        self.seat = Seat.objects.create(seat_number="B2", is_booked=False)

        # Authenticate user for protected routes
        self.client.force_authenticate(user=self.user)

    def test_get_movies_list(self):
        """Test GET request for movies list API"""
        response = self.client.get("/api/movies/")  # Ensure API prefix is correct
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_movie(self):
        """Test POST request to create a movie"""
        data = {
            "title": "Django Unchained",
            "description": "A bounty hunter frees a slave and they take down a plantation owner.",
            "release_date": "2012-12-25",
            "duration": 165
        }
        response = self.client.post("/api/movies/", data, format="json")  # Ensure correct API prefix
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_seats_list(self):
        """Test GET request for seats list API"""
        response = self.client.get("/api/seats/")  # Ensure correct API prefix
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_booking(self):
        """Test POST request to book a seat"""
        data = {
            "user": self.user.id,
            "movie": self.movie.id,
            "seat": self.seat.id
        }
        response = self.client.post("/api/bookings/", data, format="json")  # Ensure correct API prefix
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

