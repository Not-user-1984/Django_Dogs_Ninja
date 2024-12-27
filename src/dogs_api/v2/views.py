from rest_framework import viewsets
from dogs_api.models import Breed, Dog
from dogs_api.v2.serializers import BreedSerializer, DogSerializer
from django.db.models import Avg, Count, OuterRef, Subquery


class BreedViewSet(viewsets.ModelViewSet):
    queryset = Breed.objects.annotate(dogs_count=Count("dog"))
    serializer_class = BreedSerializer


class DogViewSet(viewsets.ModelViewSet):
    queryset = Dog.objects.annotate(
        same_breed_count=Count("breed__dog"),
        breed_avg_age=Subquery(
            Breed.objects.filter(id=OuterRef("breed_id"))
            .annotate(avg_age=Avg("dog__age"))
            .values("avg_age")
        ),
    ).select_related("breed")
    serializer_class = DogSerializer
