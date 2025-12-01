from rest_framework import serializers
from .models import Category, Recipe, Review, Favorite

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ['id', 'title', 'description', 'instructions', 'ingredients', 'category', 'author', 'created_at']
        read_only_fields = ['created_at', 'updated_at', 'author']

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'recipe', 'user', 'rating', 'content', 'created_at']
        read_only_fields = ['user', 'created_at']

class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = ['id', 'user', 'recipe', 'created_at']
        read_only_fields = ['user', 'created_at']