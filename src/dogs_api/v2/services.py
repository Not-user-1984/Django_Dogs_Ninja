from dogs_api.models import Breed, Dog
from django.db.models import Count, Avg, OuterRef, Subquery


class BreedService:
    @staticmethod
    def get_queryset():
        return Breed.objects.annotate(dogs_count=Count("dog"))

    @staticmethod
    def create_breed(validated_data):
        return Breed.objects.create(**validated_data)

    @staticmethod
    def update_breed(breed, validated_data):
        for attr, value in validated_data.items():
            setattr(breed, attr, value)
        breed.save()
        return breed

    @staticmethod
    def delete_breed(breed):
        breed.delete()


class DogService:
    @staticmethod
    def get_queryset():
        return Dog.objects.annotate(
            same_breed_count=Count("breed__dog"),
            breed_avg_age=Subquery(
                Dog.objects.filter(breed=OuterRef("breed"))
                .values("breed")
                .annotate(avg_age=Avg("age"))
                .values("avg_age")
            ),
        )

    @staticmethod
    def create_dog(validated_data):
        return Dog.objects.create(**validated_data)

    @staticmethod
    def update_dog(dog, validated_data):
        for attr, value in validated_data.items():
            setattr(dog, attr, value)
        dog.save()
        return dog

    @staticmethod
    def delete_dog(dog):
        dog.delete()
