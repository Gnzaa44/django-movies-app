from django.urls import path
from .views import (
    MovieListView, MovieDetailView, MovieCreateView,
    MovieUpdateView, MovieDeleteView, login_view, logout_view
)

urlpatterns = [
    path('', MovieListView.as_view(), name='movie_list'),
    path('movie/<int:pk>/', MovieDetailView.as_view(), name='movie_detail'),
    path('movies/add/', MovieCreateView.as_view(), name='movie_add'),
    path('movies/<int:pk>/edit/', MovieUpdateView.as_view(), name='movie_edit'),
    path('movies/<int:pk>/delete/', MovieDeleteView.as_view(), name='movie_delete'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]
