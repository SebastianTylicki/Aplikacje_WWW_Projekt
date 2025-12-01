from rest_framework import serializers
from .models import Category, Recipe

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ['id', 'title', 'description', 'instructions', 'ingredients', 'category', 'author', 'created_at']
        read_only_fields = ['created_at', 'updated_at']