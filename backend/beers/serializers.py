from rest_framework import serializers

from beers.models import Beer, Review, Comment


class BeerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Beer
        fields = "__all__"


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"
