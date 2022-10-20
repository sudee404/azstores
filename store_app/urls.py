from django.urls import path, include
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('product/<int:pk>',views.ProductDetailView.as_view(),name='product-detail')
]
