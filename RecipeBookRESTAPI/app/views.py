from django.contrib.auth.models import User
from django.core.serializers import get_serializer
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer
from rest_framework.schemas import AutoSchema
from rest_framework.views import APIView

from .models import Recipe, Step, Ingredient
from .serializers import SerializeRecipe,SerializeRecipeList
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView, ListCreateAPIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.


# Create your views here.

class UserCountView(APIView):
    """
    A view that returns the count of active users in JSON.
    """
    renderer_classes = [JSONRenderer]

    def get(self, request, format=None):
        html = "<html><body><center>Welcome to RecipeBookRESTAPI </br></br>Using the URLconf defined in RecipeBookRESTAPI.urls, Django tries these URL patterns:<br/><br/>admin/</br>recipes/</br>users/</br>recipes/users/recipe_id"
        return HttpResponse(html)

class ListOfRecipes(ListAPIView):
    queryset = Recipe.objects.all()
    serializer_class = SerializeRecipeList


class ListOfUsers(ListAPIView):
    def get_queryset(self):
        queryset = Recipe.objects.filter(user=self.request.user)
        return queryset
    serializer_class = SerializeRecipe


class NewRecipe(ListCreateAPIView):
     queryset = Recipe.objects.all()
     serializer_class = SerializeRecipe

     def create(self, request, *args, **kwargs):
         serializer = self.get_serializer(data=request.data)
         serializer.is_valid(raise_exception=True)
         serializer.save(user=request.user)
         return Response(serializer.data, status=status.HTTP_201_CREATED)


class RetrieveOrUpdateOrDestroyRecipe(RetrieveUpdateDestroyAPIView):
     queryset = Recipe.objects.all()
     serializer_class = SerializeRecipe