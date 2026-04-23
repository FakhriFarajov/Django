from django.shortcuts import get_object_or_404, redirect, render
from .models import Product, Review

# Create your views here.
def product_list_view(request):
    products = Product.objects.all()
    return render(request, "products/product_list.html", {
        "products": products,
    })

def product_detail_view(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    reviews = product.review_set.all()
    return render(request, "products/product_detail.html", {
        "product": product,
        "reviews": reviews,
        "user": request.user,
    })
