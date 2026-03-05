from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie




def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'movies/movie_list.html', {'movies':movies})



def movie_detail(request,pk):
    movie = get_object_or_404(Movie, pk=pk)
    return render(request, 'movies/movie_detail.html', {'movie':movie})




from django.contrib.auth.decorators import user_passes_test
from .forms import MovieForm



def is_admin(user):
    return user.is_superuser



@user_passes_test(is_admin)
def add_movie(request):
    if request.method == "POST":
        print(request.POST,"****")
        form = MovieForm(request.POST)
        print("--------------")
        if form.is_valid():
            print("%%%%%%%%%%%")
            form.save()
            print("$$$$$$$")
            return redirect('movie_list')
        else:
            print(form.errors)
    else:
        form = MovieForm()

    return render(request, 'movies/add_movie.html', {'form': form})

