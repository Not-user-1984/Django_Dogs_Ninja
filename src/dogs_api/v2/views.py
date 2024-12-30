from rest_framework import viewsets
# from rest_framework.response import Response
# from dogs_api.models import Breed, Dog
from dogs_api.v2.serializers import BreedSerializer, DogSerializer, DogListSerializer,  DogSerializer
from .services import BreedService, DogService


class BreedViewSet(viewsets.ModelViewSet):
    """
    ViewSet для работы с породами собак.
    """

    serializer_class = BreedSerializer

    def get_queryset(self):
        return BreedService.get_queryset()

    def perform_create(self, serializer):
        BreedService.create_breed(serializer.validated_data)

    def perform_update(self, serializer):
        BreedService.update_breed(
            serializer.instance, serializer.validated_data)

    def perform_destroy(self, instance):
        BreedService.delete_breed(instance)


class DogViewSet(viewsets.ModelViewSet):
    """
    ViewSet для работы с собаками.
    """
    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return DogListSerializer
        return DogSerializer

    def get_queryset(self):
        return DogService.get_queryset()

    def perform_create(self, serializer):
        DogService.create_dog(serializer.validated_data)

    def perform_update(self, serializer):
        DogService.update_dog(serializer.instance, serializer.validated_data)

    def perform_destroy(self, instance):
        DogService.delete_dog(instance)
