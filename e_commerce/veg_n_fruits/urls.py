from django.urls import path
from veg_n_fruits.views import CategoryDetailView, CategoryView

app_name = 'veg_n_fruits'

urlpatterns = [
    path('<int:pk>/', CategoryDetailView.as_view(), name=''),
    path('', CategoryView.as_view(), name="home")
]
