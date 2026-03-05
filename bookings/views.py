from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from movies.models import Movie
from .models import Booking
from .forms import BookingForm







@login_required
def book_ticket(request, pk):
    movie = get_object_or_404(Movie, pk=pk)


    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            seats = form.cleaned_data['seats']

            if seats <= movie.available_seats:
                total = seats * movie.price

                movie.available_seats -= seats
                movie.save()

                Booking.objects.create(
                    user=request.user,
                    movie=movie,
                    seats=seats,
                    total_price=total
                )

                messages.success(request, "Booking successful!")
                return redirect('my_bookings')
            else:
                messages.error(request, "Not enough seats available")
    else:
        form = BookingForm()

    return render(request, 'bookings/book_ticket.html', {'form': form, 'movie': movie})





@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'bookings/my_bookings.html', {'bookings': bookings})




def cancel_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    
    movie = booking.movie

    movie.available_seats += booking.seats
    movie.save()

    booking.delete()

    messages.success(request, "booking cancelled successfully")

    return redirect('my_bookings')




