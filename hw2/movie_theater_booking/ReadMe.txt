Movie Theater Booking App

Setup
-clone repository

git clone https://github.com/KabelNoah/cs4300
cd /home/student/cs4300/hw2/movie_theater_booking

-create virtual enviroment
python3 -m venv myenv
source myenv/bin/activate
pip install django djangorestframework

-run app through devedu
python manage.py runserver 0.0.0.0:3000

-Access the App
Main Page: http://localhost/proxy/3000/
Book Seats: http://localhost/proxy/3000/book/"ID-FOR-GIVEN-MOVIE"/
Booking History: http://localhost/proxy/3000/booking_history/
Admin Panel: http://localhost/proxy/3000/admin/


-API Endpoints
Movies: GET /api/movies/
Seats: GET /api/seats/
Bookings: POST /api/bookings/

This project was developed with assistance from **ChatGPT (GPT-4)** for:
- Debugging Django errors
- Implementing functionality (API endpoints, unique seats per movie, fixing redirects, Database implementation, HTML for all pages, creating unit tests)
