from django.urls import path
from . import views

urlpatterns = [
    path('categories/', views.category_list, name='category-list'),
    path('recipes/', views.recipe_list, name='recipe-list'),
    path('recipes/<int:pk>/', views.recipe_detail, name='recipe-detail'),
    path('recipes/<int:recipe_pk>/review/', views.add_review, name='add-review'),
    path('recipes/<int:recipe_pk>/favorite/', views.manage_favorite, name='manage-favorite'),
]