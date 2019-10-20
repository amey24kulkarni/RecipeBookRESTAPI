from django.urls import path, include
from .views import ListOfRecipes,ListOfUsers,NewRecipe, RetrieveOrUpdateOrDestroyRecipe, UserCountView

app_name = 'RecipeBookRESTAPI'

urlpatterns = [
    path('',UserCountView.as_view()),
    path('recipes/',ListOfRecipes.as_view()),
    path('users/',ListOfUsers.as_view()),
    path('recipes/',NewRecipe.as_view()),
    path('recipes/users/<int:pk>/',RetrieveOrUpdateOrDestroyRecipe.as_view())
]