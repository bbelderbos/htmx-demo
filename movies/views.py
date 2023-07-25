from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import QueryDict
from django.views.decorators.http import require_http_methods
from django.http import HttpResponse
from .models import Movie

NUMBER_MOVIES_PER_PAGE = 20

def movie_list(request):
    movies = Movie.objects.all()[:NUMBER_MOVIES_PER_PAGE]
    context = {
        'movies': movies,
        'next_page': 1,
    }
    return render(request, 'movies/movie_list.html', context)


def get_more_movies(request):
    try:
        page_number = int(request.GET.get("page", 1))
    except ValueError:
        context = {
            'movies': [], 'next_page': None,
        }
        return render(request, 'movies/_movies.html', context)

    movies = Movie.objects.all()
    paginator = Paginator(movies, NUMBER_MOVIES_PER_PAGE)
    page = paginator.get_page(page_number)

    context = {
        'movies': page.object_list,
        'next_page': page_number + 1 if page.has_next() else None,
    }
    return render(request, 'movies/_movies.html', context)


@require_http_methods(['DELETE'])
def delete_movie(request, pk):
    try:
        movie = Movie.objects.get(pk=pk)
    except Movie.DoesNotExist:
        return HttpResponse(status=404)
    else:
        movie.delete()
    return HttpResponse(status=200)


def edit_movie(request, pk):
    try:
        movie = Movie.objects.get(pk=pk)
    except Movie.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'PUT':
        qd = QueryDict(request.body.decode())
        movie.title = qd['title']
        movie.genre = qd['genre']
        movie.save()
        # render the initial static html with movie
        return render(request, 'movies/_movie_detail.html', {'movie': movie})

    # if user cancels out of form, show static html again
    if request.GET.get("cancel", False):
        return render(request, 'movies/_movie_detail.html', {'movie': movie})

    # render the form
    genres = Movie.objects.values_list(
        'genre', flat=True
    ).distinct().order_by("genre")
    context = {'movie': movie, 'genres': genres}
    return render(request, 'movies/_movie_form.html', context)


def search_movies(request):
    search = request.POST.get('search', '')
    if search:
        movies = Movie.objects.filter(title__icontains=search)
    else:
        movies = Movie.objects.all()[:NUMBER_MOVIES_PER_PAGE]
    return render(request, 'movies/_movies.html', {'movies': movies})


def show_movie(request, pk):
    try:
        movie = Movie.objects.get(pk=pk)
    except Movie.DoesNotExist:
        return HttpResponse(status=404)

    context = {'movie': movie}
    return render(request, 'movies/movie.html', context)
