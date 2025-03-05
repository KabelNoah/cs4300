from django.http import HttpResponse
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MovieViewSet, SeatViewSet, BookingViewSet, movie_list, seat_booking, booking_history

# Use a router to handle API endpoints automatically
router = DefaultRouter()
router.register(r'movies', MovieViewSet)
router.register(r'seats', SeatViewSet)
router.register(r'bookings', BookingViewSet)

urlpatterns = [
    path('api/', include(router.urls)),  # Include API endpoints
    path('', movie_list, name='movie_list'),
    path('book/<int:movie_id>/', seat_booking, name='seat_booking'),
    path('booking_history/', booking_history, name='booking_history'), 
]