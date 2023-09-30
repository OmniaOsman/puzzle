from django.urls import path
from . import views

urlpatterns = [
    path('puzzles/', views.GetPuzzleAPIView.as_view(), name='puzzle_GET'),
    path('puzzles/<int:id>', views.GetPuzzleAPIView.as_view(), name='puzzle_GET'),
    path('puzzles/create', views.PostPuzzleApiView.as_view(), name='puzzle_POST'),
]
 