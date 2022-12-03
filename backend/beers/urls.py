from django.urls import path

from beers import views

urlpatterns = [
    path('', views.api_overview),
    path('beers/', views.beers_list),
    path('beers/<int:beer_pk>/', views.beer_detail),
    path('beers/<int:beer_pk>/reviews/', views.reviews_list),
    path('beers/<int:beer_pk>/reviews/<int:review_pk>/', views.review_details),
    path('beers/<int:beer_pk>/reviews/<int:review_pk>/comments/', views.comments_list),
    path('beers/<int:beer_pk>/reviews/<int:review_pk>/comments/<int:comment_pk>/', views.comment_detail),

]