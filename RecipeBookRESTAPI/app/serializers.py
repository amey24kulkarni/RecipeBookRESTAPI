from rest_framework import serializers
from .models import Recipe, Step, Ingredient





class SerializeRecipe(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = "__all__"


class SerializeStep(serializers.ModelSerializer):
    class Meta:
        model = Step
        fields = "__all__"


class SerializeIngredient(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = "__all__"


class SerializeRecipeList(serializers.ModelSerializer):
    step = serializers.SerializerMethodField()
    ingredient = serializers.SerializerMethodField()

    def get_step(self, obj):
        step = obj.Recipe_Step
        serializer = SerializeStep(step, many=True).data
        return serializer

    def get_ingredient(self, obj):
        ingredient = obj.Recipe_Ingredient
        serializer = SerializeIngredient(ingredient, many=True).data
        return serializer

    class Meta:
        model = Recipe
        fields = "__all__"
