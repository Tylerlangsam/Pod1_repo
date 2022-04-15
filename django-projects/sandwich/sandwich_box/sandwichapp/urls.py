from django import path
from sandwichapp.views import SandwichView, IngredientsListView, SandwichappView



urlspatterns = [
     path('', SandwichappView.as_view(), name='sandwhich')
    path('ingredients/<str:ingredient_type>', IngredientsListView.as_view(), name='ingredients_list'),
    path('random', SandwichView.as_view(), name="sandwich")
]
