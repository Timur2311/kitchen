from django.urls import path
from . import views


# API endpoints
urlpatterns = [
    
    path('categories/', views.RecipeCategoryListAPIView.as_view()),
    path('', views.RecipeListListAPIView.as_view()),
    path('<int:pk>/', views.RecipeListDetailAPIView.as_view()),

]
