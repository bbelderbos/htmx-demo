from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.movie_list, name='movie_list'),
    path('movies', views.get_more_movies, name='get_more_movies'),
    path('search', views.search_movies, name='search_movies'),
    path('<int:pk>', views.show_movie, name='show_movie'),
    path('<int:pk>/delete', views.delete_movie, name='delete_movie'),
    path('<int:pk>/edit', views.edit_movie, name='edit_movie'),
]
