from django.urls import path
# from rest_framework.urlpatterns import format_suffix_patterns
from . import views





# API endpoints
urlpatterns = [
    
    path('categories/', views.CategoryList.as_view()),
    path('', views.RecipeList.as_view()),
    path('<slug:slug>/', views.RecipeDetail.as_view()),

]