from django.urls import path
from . import views

app_name = "reviews"

urlpatterns = [
    path('<int:product_id>/add/', views.review_create, name='add'),
    path('<int:review_id>/edit/', views.review_update, name='edit'),
    path('<int:review_id>/delete/', views.review_delete, name='delete'),
]