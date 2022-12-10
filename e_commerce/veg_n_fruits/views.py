from django.shortcuts import render
from django.views.generic import ListView, DetailView
from veg_n_fruits.models import Category, ItemDetails

# Create your views here.


# class IndexView(TemplateView):
#     template_name = 'veg_n_fruits/index.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["key"] = 'This is from Template view'
#         return(context)

class CategoryView(ListView):
    template_name = 'veg_n_fruits/index.html'
    model = Category
    context_object_name = 'category'


class CategoryDetailView(DetailView):
    template_name = 'veg_n_fruits/category_details.html'
    model = Category
    context_object_name = 'namelist'
