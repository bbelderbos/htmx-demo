from django.core.paginator import Paginator
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.http import HttpResponse
from .models import Movie

NUMBER_MOVIES_PER_PAGE = 20

def movie_list(request):
    movies = Movie.objects.all()[:NUMBER_MOVIES_PER_PAGE]
    return render(request, 'movies/movie_list.html', {'movies': movies})


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
