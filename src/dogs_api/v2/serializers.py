from rest_framework import serializers
from dogs_api.models import Breed, Dog
from django.db.models import Avg, Count, OuterRef, Subquery


class BreedSerializer(serializers.ModelSerializer):
    dogs_count = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Breed
        fields = [
            "id",
            "name",
            "size",
            "friendliness",
            "trainability",
            "shedding_amount",
            "exercise_needs",
            "dogs_count",
        ]

    def get_dogs_count(self, obj):
        return obj.dogs_count if hasattr(obj, "dogs_count") else None


class DogSerializer(serializers.ModelSerializer):
    breed = BreedSerializer(read_only=True)
    same_breed_count = serializers.SerializerMethodField()
    breed_avg_age = serializers.SerializerMethodField()

    class Meta:
        model = Dog
        fields = [
            "id",
            "name",
            "age",
            "breed",
            "gender",
            "color",
            "favorite_food",
            "favorite_toy",
            "same_breed_count",
            "breed_avg_age",
        ]

    def get_same_breed_count(self, obj):
        return obj.same_breed_count

    def get_breed_avg_age(self, obj):
        return obj.breed_avg_age
