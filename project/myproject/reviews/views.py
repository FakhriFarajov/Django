from django.http import HttpResponse, HttpRequest, HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CreateReview
from .models import Review, Product

# Create your views here.

@login_required
def review_create(request: HttpRequest, product_id: int):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == "POST":
        form = CreateReview(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.author = request.user
            review.product = product
            review.save()
            form.save_m2m()
            messages.success(request, "Review Created")
            return redirect("products:detail", pk=product.pk)
    else:
        form = CreateReview()
    return render(request, "reviews/review_form.html", {"form": form, "mode": "create", "product": product})

@login_required
def review_update(request: HttpRequest, review_id: int) -> HttpResponse:
    review = get_object_or_404(Review, pk=review_id)
    if review.author != request.user:
        return HttpResponseForbidden("You are not allowed to edit this review.")
    if request.method == "POST":
        form = CreateReview(request.POST, instance=review)
        if form.is_valid():
            form.save()
            messages.success(request, "Review Updated")
            return redirect("products:detail", pk=review.product.pk)
    else:
        form = CreateReview(instance=review)
    return render(request, "reviews/review_form.html", {"form": form, "mode": "edit", "review": review})

@login_required
def review_delete(request: HttpRequest, review_id: int) -> HttpResponse:
    review = get_object_or_404(Review, pk=review_id)
    if review.author != request.user:
        return HttpResponseForbidden("You are not allowed to delete this review.")
    product_id = review.product.pk
    if request.method == "POST":
        review.delete()
        messages.success(request, "Review Deleted")
        return redirect("products:detail", pk=product_id)
    return render(request, "reviews/review_confirm_delete.html", {"review": review})
