from django.db import models




class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    release_date = models.DateField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    total_seats = models.IntegerField()
    available_seats = models.IntegerField()

    def __str__(self):
        return self.title