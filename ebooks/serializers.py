from .models import Ebook, Review
from rest_framework import serializers



class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        # fields = "__all__"
        exclude = ("ebook",)

class EbookSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True,read_only=True)
    class Meta:
        model = Ebook
        fields = "__all__"
