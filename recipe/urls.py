from django.urls import path
from . import views

# API endpoints
urlpatterns = [
    path('', views.saving_data)
    # path('categories/', views.CategoryList.as_view()),
    # path('', views.RecipeList.as_view()),
    # path('<slug:slug>/', views.RecipeDetail.as_view()),

]
