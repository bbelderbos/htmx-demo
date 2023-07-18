from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.http import HttpResponse
from .models import Movie

NUMBER_MOVIES_PER_PAGE = 20

def movie_list(request):
    movies = Movie.objects.all()[:NUMBER_MOVIES_PER_PAGE]
    return render(request, 'movies/movie_list.html', {'movies': movies})


def get_more_movies(request):
    page = int(request.GET["page"])
    # TODO: what if I go beyond the number of movies?
    movies = Movie.objects.all()[page*NUMBER_MOVIES_PER_PAGE:(page+1)*NUMBER_MOVIES_PER_PAGE]
    print(f"called get_more_movies with page {page}")
    print([mo.id for mo in movies])
    context = {
        'movies': movies,
        'next_page': page + 1,
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
