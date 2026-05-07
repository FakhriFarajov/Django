from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from . import models, forms


@login_required
def my_movies(request):
    movies = models.Movie.objects.filter(author=request.user)

    selected_status = request.GET.get("status", "").strip()
    selected_genre = request.GET.get("genre", "").strip()

    valid_statuses = {choice[0] for choice in models.STATUS_CHOICES}
    if selected_status in valid_statuses:
        movies = movies.filter(status=selected_status)

    if selected_genre:
        movies = movies.filter(genre__iexact=selected_genre)

    genres = (
        models.Movie.objects
        .filter(author=request.user)
        .order_by("genre")
        .values_list("genre", flat=True)
        .distinct()
    )

    return render(
        request,
        "main/my_movies.html",
        {
            "movies": movies,
            "status_choices": models.STATUS_CHOICES,
            "genres": genres,
            "selected_status": selected_status,
            "selected_genre": selected_genre,
        },
    )


@login_required
def create_movie(request):
    if request.method == "POST":
        form = forms.CreateMovieForm(request.POST)
        if form.is_valid():
            movie = form.save(commit=False)
            movie.author = request.user
            movie.save()
            return redirect('watchlist:my_movies')
    else:
        form = forms.CreateMovieForm()
    return render(request, "main/add_movie.html", {'form': form})


@login_required
def edit_movie(request, movie_id):
    movie = get_object_or_404(models.Movie, id=movie_id, author=request.user)
    if request.method == "POST":
        form = forms.UpdateMovieForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('watchlist:my_movies')
    else:
        form = forms.UpdateMovieForm(instance=movie)
    return render(request, "main/edit_movie.html", {'form': form, 'movie': movie})


@login_required
def delete_movie(request, movie_id):
    movie = get_object_or_404(models.Movie, id=movie_id, author=request.user)
    if request.method == "POST":
        movie.delete()
        return redirect('watchlist:my_movies')
    return render(request, "main/delete_movie.html", {'movie': movie})
