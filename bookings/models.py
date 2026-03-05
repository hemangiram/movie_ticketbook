from django.db import models
from django.contrib.auth.models import User
from movies.models import Movie




class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    seats = models.IntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    booking_time = models.DateTimeField(auto_now_add=True)



    
