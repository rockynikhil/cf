from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from testapp.models import Beer

# Create your views here.
class BeerListView(ListView):
    model = Beer
    #t_f = beer_list.html
    #c_o_n: beer_list

class BeerDetailView(DetailView):
    model = Beer
    #t_f:beer_detail.views
    #c_o_n:beer or object

class BeerCreateView(CreateView):
    model = Beer
    fields = '__all__'
   # t_f:beer_form.html


class BeerUpdateView(UpdateView):
    model = Beer
    fields = '__all__'
    #t_f:beer_form.html

from django.urls import reverse_lazy
class BeerDeleteView(DeleteView):
    model = Beer
    success_url = reverse_lazy('list')



