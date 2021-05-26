from django.shortcuts import render
from rest_framework import mixins, generics
from .models import Ebook, Review
from .serializers import EbookSerializer, ReviewSerializer
from rest_framework.generics import get_object_or_404

# Create your views here.

#  USING CONCRETE API VIEW CLASS
class EbookListCreateAPIView(generics.ListCreateAPIView):
    queryset  = Ebook.objects.all()
    serializer_class = EbookSerializer

class EbookDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset  = Ebook.objects.all()
    serializer_class = EbookSerializer

class ReviewCreateAPIView(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def perform_create(self, serializer):
        ebook_pk = self.kwargs.get("ebook_pk")
        ebook = get_object_or_404(Ebook, pk=ebook_pk)
        serializer.save(ebook=ebook)

class ReviewDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = EbookSerializer






# USING MIXIN CLASS
# class EbookListCreateApiView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
#     queryset  = Ebook.objects.all()
#     serializer_class = EbookSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)