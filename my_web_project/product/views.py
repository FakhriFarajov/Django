from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ReviewForm
from .models import Product, Review

def product_list(request):
    products = Product.objects.all()
    return render(request, "product/product_list.html", {"products": products})

def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    reviews = product.reviews.select_related('user').all()
    review_form = None
    if request.user.is_authenticated:
        # Only allow one review per user per product
        if not product.reviews.filter(user=request.user).exists():
            review_form = ReviewForm()
    if request.method == 'POST' and review_form is not None:
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            review.user = request.user
            review.save()
            return redirect('product_detail', pk=product.id)
    return render(request, 'product/product_detail.html', {'product': product, 'reviews': reviews, 'review_form': review_form})


@login_required
def review_add(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            review.user = request.user
            review.save()
            return redirect('product_detail', pk=product.id)
    else:
        form = ReviewForm()
    return render(request, 'product/review_form.html', {'form': form, 'product': product})


@login_required
def review_edit(request, review_id):
    review = get_object_or_404(Review, pk=review_id, user=request.user)
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect('product_detail', pk=review.product.id)
    else:
        form = ReviewForm(instance=review)
    return render(request, 'product/review_form.html', {'form': form, 'product': review.product, 'edit': True})


@login_required
def review_delete(request, review_id):
    review = get_object_or_404(Review, pk=review_id, user=request.user)
    product_id = review.product.id
    if request.method == 'POST':
        review.delete()
        return redirect('product_detail', pk=product_id)
    return render(request, 'product/review_confirm_delete.html', {'review': review})
