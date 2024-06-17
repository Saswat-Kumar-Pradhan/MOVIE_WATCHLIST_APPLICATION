from django.shortcuts import render, get_object_or_404, redirect
from .models import Movie
from .forms import MovieForm

def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'movie_list.html', {'movies': movies})

def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    return render(request, 'movie_detail.html', {'movie': movie})

def movie_create(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('movie_list')
    else:
        form = MovieForm()
    return render(request, 'movie_form.html', {'form': form})

def movie_update(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    if request.method == 'POST':
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('movie_list')
    else:
        form = MovieForm(instance=movie)
    return render(request, 'movie_form.html', {'form': form})

def movie_delete(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    if request.method == 'POST':
        movie.delete()
        return redirect('movie_list')
    return render(request, 'movie_confirm_delete.html', {'movie': movie})
