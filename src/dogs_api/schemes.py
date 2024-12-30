from ninja import Schema
from typing import Optional
from pydantic import ConfigDict


class BaseSchema(Schema):
    """Абстрактная базовая схема с общей конфигурацией."""

    model_config = ConfigDict(from_attributes=True)


class BaseBreedSchema(BaseSchema):
    """Базовая схема для модели Breed."""

    model_config = ConfigDict(from_attributes=True)
    name: str
    size: str
    friendliness: int
    trainability: int
    shedding_amount: int
    exercise_needs: int


class BaseDogSchema(BaseSchema):
    """Базовая схема для модели Dog."""
    model_config = ConfigDict(from_attributes=True)
    name: str
    age: int
    breed_id: int
    gender: str
    color: str
    favorite_food: str
    favorite_toy: str


class BreedListSchema(BaseSchema):
    """Схема для списка пород с количеством собак."""

    dogs_count: Optional[int] = None


class BreedDetailSchema(BaseSchema):
    """Схема для детальной информации о породе."""

    dogs_count: Optional[int] = None


class DogListSchema(BaseSchema):
    """Схема для списка собак с дополнительной информацией."""

    breed: BaseBreedSchema
    breed_avg_age: Optional[float] = None


class DogDetailSchema(BaseSchema):
    """Схема для детальной информации о собаке."""

    breed: BaseBreedSchema
    same_breed_count: Optional[int] = None
