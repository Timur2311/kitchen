from django.urls import path
from . import views
from recipe.helpers import backup

# API endpoints
urlpatterns = [
    path('',backup.perform_backup)
    # path('categories/', views.CategoryList.as_view()),
    # path('', views.RecipeList.as_view()),
    # path('<slug:slug>/', views.RecipeDetail.as_view()),

]
