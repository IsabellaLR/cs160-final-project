from django.urls import path

from . import views

urlpatterns = [
    path('browseSalads/', views.browseSalads, name='browseSalads'),
    path('similarSalads/', views.similarSalads, name='similarSalads'),
    path('viewIngredients/', views.viewIngredients, name='viewIngredients'),
    path('alternateIngredients/', views.alternateIngredients, name='alternateIngredients'),
    path('viewInstructions/', views.viewInstructions, name='viewInstructions'),
    path('shopIngredients/', views.shopIngredients, name='shopIngredients'),
    path('', views.index, name='index'),
]
