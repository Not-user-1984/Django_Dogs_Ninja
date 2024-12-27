from django.shortcuts import render

from django.db.models import Avg, OuterRef, Subquery, Count
from ninja import NinjaAPI
from .models import Dog, Breed
import dogs_api.schemes as schemes

api = NinjaAPI()


@api.post("/breeds/")
def create_breed(request, breed: schemes.BaseBreedSchema):
    """Создание новой породы."""
    breed_data = breed.dict()
    breed_instance = Breed.objects.create(**breed_data)
    return {"id": breed_instance.id}


@api.get("/breeds/", response=list[schemes.BreedListSchema])
def list_breeds(request):
    """Получение списка всех пород."""
    breeds = Breed.objects.annotate(dogs_count=Count("dog"))
    return breeds


@api.get("/breeds/{breed_id}", response=schemes.BreedDetailSchema)
def get_breed(request, breed_id: int):
    """Получение информации о конкретной породе."""
    breed = Breed.objects.annotate(dogs_count=Count("dog")).get(id=breed_id)
    return breed


@api.put("/breeds/{breed_id}")
def update_breed(request, breed_id: int, breed: schemes.BaseBreedSchema):
    """Обновление информации о породе."""
    breed_data = breed.dict()
    Breed.objects.filter(id=breed_id).update(**breed_data)
    return {"success": True}


@api.delete("/breeds/{breed_id}")
def delete_breed(request, breed_id: int):
    """Удаление породы."""
    Breed.objects.filter(id=breed_id).delete()
    return {"success": True}


@api.post("/dogs/")
def create_dog(request, dog: schemes.BaseDogSchema):
    """Создание новой собаки."""
    dog_data = dog.dict()
    dog_instance = Dog.objects.create(**dog_data)
    return {"id": dog_instance.id}


@api.get("/dogs/", response=list[schemes.DogListSchema])
def list_dogs(request):
    """Получение списка всех собак."""
    avg_age_subquery = (
        Breed.objects.filter(id=OuterRef("breed_id"))
        .annotate(avg_age=Avg("dog__age"))
        .values("avg_age")
    )
    dogs = Dog.objects.annotate(
        breed_avg_age=Subquery(avg_age_subquery)
    ).select_related("breed")
    return dogs


@api.get("/dogs/{dog_id}", response=schemes.DogDetailSchema)
def get_dog(request, dog_id: int):
    """Получение информации о конкретной собаке."""
    dog = (
        Dog.objects.annotate(same_breed_count=Count("breed__dog"))
        .select_related("breed")
        .get(id=dog_id)
    )
    return dog


@api.put("/dogs/{dog_id}")
def update_dog(request, dog_id: int, dog: schemes.BaseDogSchema):
    """Обновление информации о собаке."""
    dog_data = dog.dict()
    Dog.objects.filter(id=dog_id).update(**dog_data)
    return {"success": True}


@api.delete("/dogs/{dog_id}")
def delete_dog(request, dog_id: int):
    """Удаление собаки."""
    Dog.objects.filter(id=dog_id).delete()
    return {"success": True}
