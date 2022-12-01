from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from beers.models import Beer, Review, Comment
from beers.serializers import BeerSerializer, ReviewSerializer, CommentSerializer


@api_view(['GET'])
def api_overview(request):
    api = {
        'Beers': '/api/v1/beers/',
        'Reviews': 'api/v1/reviews/<int:beer_pk>/',
        'Comments': 'api/v1/comments/<int:review_pk>/'
    }
    return Response(api)


@api_view(['GET', 'POST'])
def beers_list(request):
    if request.method == 'GET':
        beers = Beer.objects.filter()
        serializer = BeerSerializer(beers, many=True)
        return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def beer_detail(request, beer_pk):
    try:
        beer = Beer.objects.get(pk=beer_pk)
    except Beer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BeerSerializer(beer)
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def reviews_list(request, beer_pk):
    if request.method == 'GET':
        reviews = Review.objects.filter(beer=beer_pk)
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def review_details(request, beer_pk, review_pk):
    try:
        beer = Beer.objects.get(pk=beer_pk)
        review = Review.objects.get(pk=review_pk)
    except Beer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    except Review.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ReviewSerializer(review)
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def comments_list(request, beer_pk, review_pk):
    if request.method == 'GET':
        comments = Comment.objects.filter(review=review_pk)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def comment_detail(request, beer_pk, review_pk, comment_pk):
    try:
        beer = Beer.objects.get(pk=beer_pk)
        review = Review.objects.get(pk=review_pk)
        comment = Comment.objects.get(pk=comment_pk)
    except Beer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    except Review.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    except Comment.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)