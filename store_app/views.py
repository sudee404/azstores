from django.shortcuts import render
from django.views.generic import DetailView
from store_app.models import Product

# Create your views here.
def index(request):
    return render(request,'index.html',{})

class ProductDetailView(DetailView):
	model = Product
