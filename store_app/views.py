from django.shortcuts import render
from django.views.generic import DetailView
from store_app.models import Product

# Create your views here.


def index(request):
    latest_men = Product.objects.filter(gender='M')
    return render(request, 'index.html', {
        'count': [1, 2, 3, 4, 5],
        'lm': latest_men,
    })


class ProductDetailView(DetailView):
    model = Product
