from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('<int:pk>/', views.product_detail, name='product_detail'),
    path('<int:product_id>/review/add/', views.review_add, name='review_add'),
    path('review/<int:review_id>/edit/', views.review_edit, name='review_edit'),
    path('review/<int:review_id>/delete/', views.review_delete, name='review_delete'),
]
