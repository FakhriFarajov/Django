from django.urls import path
from . import views
from reviews import views as review_views

app_name = "products"

urlpatterns = [
    path('', views.product_list_view, name='list'),
    path('<int:product_id>/', views.product_detail_view, name='detail'),
    path('<int:product_id>/reviews/add/', review_views.review_create, name='review_add'),
    path('reviews/<int:review_id>/edit/', review_views.review_update, name='review_edit'),
    path('reviews/<int:review_id>/delete/', review_views.review_delete, name='review_delete'),
]