# Generated by Django 5.1.4 on 2024-12-25 06:44

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Breed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название породы')),
                ('size', models.CharField(choices=[('Tiny', 'Tiny'), ('Small', 'Small'), ('Medium', 'Medium'), ('Large', 'Large')], max_length=10, verbose_name='Размер')),
                ('friendliness', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)], verbose_name='Дружелюбие')),
                ('trainability', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)], verbose_name='Дрессируемость')),
                ('shedding_amount', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)], verbose_name='Количество выпадающей шерсти')),
                ('exercise_needs', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)], verbose_name='Потребность в упражнениях')),
            ],
            options={
                'verbose_name': 'Порода',
                'verbose_name_plural': 'Породы',
            },
        ),
        migrations.CreateModel(
            name='Dog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя собаки')),
                ('age', models.PositiveIntegerField(verbose_name='Возраст')),
                ('gender', models.CharField(max_length=50, verbose_name='Пол')),
                ('color', models.CharField(max_length=50, verbose_name='Цвет')),
                ('favorite_food', models.CharField(max_length=100, verbose_name='Любимая еда')),
                ('favorite_toy', models.CharField(max_length=100, verbose_name='Любимая игрушка')),
                ('breed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dogs_api.breed', verbose_name='Порода')),
            ],
            options={
                'verbose_name': 'Собака',
                'verbose_name_plural': 'Собаки',
            },
        ),
    ]
