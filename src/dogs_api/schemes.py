from ninja import Schema
from typing import Optional


class BaseBreedSchema(Schema):
    """Базовая схема для модели Breed."""

    name: str
    size: str
    friendliness: int
    trainability: int
    shedding_amount: int
    exercise_needs: int


class BaseDogSchema(Schema):
    """Базовая схема для модели Dog."""
    name: str
    age: int
    breed_id: int
    gender: str
    color: str
    favorite_food: str
    favorite_toy: str


class BreedListSchema(BaseBreedSchema):
    """Схема для списка пород с количеством собак."""

    dogs_count: Optional[int] = None


class BreedDetailSchema(BaseBreedSchema):
    """Схема для детальной информации о породе."""

    dogs_count: Optional[int] = None


class DogListSchema(BaseDogSchema):
    """Схема для списка собак с дополнительной информацией."""

    breed: BaseBreedSchema
    breed_avg_age: Optional[float] = None


class DogDetailSchema(BaseDogSchema):
    """Схема для детальной информации о собаке."""

    breed: BaseBreedSchema
    same_breed_count: Optional[int] = None
