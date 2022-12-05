from django.urls import path

from beers import views

urlpatterns = [
    path('', views.api_overview),
    path('beers/', views.beers_list),
    path('beers/<int:beer_pk>/', views.beer_detail),
    path('reviews/', views.reviews_list),
    path('reviews/<int:review_pk>/', views.review_details),
    path('comments/', views.comments_list),
    path('comments/<int:comment_pk>/', views.comment_detail),

]