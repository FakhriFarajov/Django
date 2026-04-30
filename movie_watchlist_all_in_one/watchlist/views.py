from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from . import models, forms


# Create your views here.
@login_required
def my_movies(request):
    movies = models.Movie.objects.filter(author=request.user)
    return render(request, "main/my_movies.html", {'movies': movies})

@login_required
def create_movie(request):
    if request.method == "POST":
        form = forms.CreateMovieForm(request.POST)
        if form.is_valid():
            movie = models.Movie(
                title=form.cleaned_data['title'],
                genre=form.cleaned_data['genre'],
                year=form.cleaned_data['release_year'],
                status=form.cleaned_data['status'],
                rating=form.cleaned_data['rating'],
                author=request.user
            )
            movie.save()
            return redirect('watchlist:my_movies')
    else:
        form = forms.CreateMovieForm()
    return render(request, "main/add_movie.html", {'form': form})

@login_required
def edit_movie(request, movie_id):
    movie = get_object_or_404(models.Movie, id=movie_id, author=request.user)
    if request.method == "POST":
        form = forms.UpdateMovieForm(request.POST)
        if form.is_valid():
            movie.title = form.cleaned_data['title']
            movie.genre = form.cleaned_data['genre']
            movie.year = form.cleaned_data['release_year']
            movie.status = form.cleaned_data['status']
            movie.rating = form.cleaned_data['rating']
            movie.save()
            return redirect('watchlist:my_movies')
    else:
        form = forms.UpdateMovieForm(initial={
            'title': movie.title,
            'genre': movie.genre,
            'release_year': movie.year,
            'status': movie.status,
            'rating': movie.rating,
        })
    return render(request, "main/edit_movie.html", {'form': form, 'movie': movie})

@login_required
def delete_movie(request, movie_id):
    movie = get_object_or_404(models.Movie, id=movie_id, author=request.user)
    if request.method == "POST":
        movie.delete()
        return redirect('watchlist:my_movies')
    return render(request, "main/delete_movie.html", {'movie': movie})
