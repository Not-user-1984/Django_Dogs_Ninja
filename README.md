
# Django Dogs Ninja

Проект для управления данными о породах собак и собаках. Включает API для создания, чтения, обновления и удаления записей.

---

## Содержание

1. [Описание](#описание)
2. [Технологии](#технологии)
3. [Установка](#установка)
4. [Настройка](#настройка)
5. [Запуск](#запуск)
6. [API](#api)
7. [Экспериментальный API (v1)](#экспериментальный-api-v1)
8. [Тестирование](#тестирование)
9. [Структура проекта](#структура-проекта)


---
## Видео

```
https://disk.yandex.ru/i/jMu3qiWOJm_glw
```

## Описание

Проект предоставляет REST API для управления данными о породах собак и собаках. Основные функции:
- Создание, чтение, обновление и удаление пород собак.
- Создание, чтение, обновление и удаление собак.
- Подсчет количества собак для каждой породы.
- Расчет среднего возраста собак для каждой породы.

---

## Технологии

- **Python** (3.12)
- **Django** (5.1)
- **Django REST Framework** (DRF)
- **NinjaAPI** (экспериментальный API)
- **PostgreSQL** (15)
- **Docker** и **Docker Compose**
- **Gunicorn** (для production)
- **pytest** (для тестирования)

---
## Установка

1. **Клонируйте репозиторий:**

   ```bash
   git clone git@github.com:Not-user-1984/Django_Dogs_Ninja.git
   ```


## Настройка

1. **Создайте файл `.env`:**

   Скопируйте `.env.example` в `.env` и настройте переменные окружения:

   ```env
   # Настройки Django
   SECRET_KEY=your_secret_key
   DEBUG=True
   ALLOWED_HOSTS=*

   # Настройки PostgreSQL
   POSTGRES_DB=dogs_db
   POSTGRES_USER=dogs_user
   POSTGRES_PASSWORD=dogs_password
   POSTGRES_HOST=db
   POSTGRES_PORT=5432
   ```

2. **Настройте базу данных:**

   Убедитесь, что PostgreSQL запущен и доступен. Обновите настройки в `settings.py`:

   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': os.getenv('POSTGRES_DB'),
           'USER': os.getenv('POSTGRES_USER'),
           'PASSWORD': os.getenv('POSTGRES_PASSWORD'),
           'HOST': os.getenv('POSTGRES_HOST'),
           'PORT': os.getenv('POSTGRES_PORT'),
       }
   }
   ```

---

### С Docker

1. **Соберите и запустите контейнеры:**

   ```bash
   docker-compose up --build
   ```


### Без Docker

2. **Создайте виртуальное окружение:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # Для Linux/MacOS
   venv\Scripts\activate     # Для Windows
   ```

3. **Установите зависимости:**

   ```bash
   pip install -r requirements.txt
   ```
4. **Запустите сервер::**

   ```bash
   python manage.py runserver
   ```

## API

### Породы собак

- **GET /api/v2/breeds/** — Список всех пород.
- **POST /api/v2/breeds/** — Создание новой породы.
- **GET /api/v2/breeds/{id}/** — Детали породы.
- **PUT /api/v2/breeds/{id}/** — Обновление породы.
- **DELETE /api/v2/breeds/{id}/** — Удаление породы.

### Собаки

- **GET /api/v2/dogs/** — Список всех собак.
- **POST /api/v2/dogs/** — Создание новой собаки.
- **GET /api/v2/dogs/{id}/** — Детали собаки.
- **PUT /api/v2/dogs/{id}/** — Обновление собаки.
- **DELETE /api/v2/dogs/{id}/** — Удаление собаки.

---

## Экспериментальный API (v1)

В качестве эксперимента в проекте реализован API на основе **NinjaAPI** с теми же эндпоинтами, что и в основной версии.

### Породы собак

- **GET /api/v1/breeds/** — Список всех пород.
- **POST /api/v1/breeds/** — Создание новой породы.
- **GET /api/v1/breeds/{breed_id}/** — Детали породы.
- **PUT /api/v1/breeds/{breed_id}/** — Обновление породы.
- **DELETE /api/v1/breeds/{breed_id}/** — Удаление породы.

### Собаки

- **GET /api/v1/dogs/** — Список всех собак.
- **POST /api/v1/dogs/** — Создание новой собаки.
- **GET /api/v1/dogs/{dog_id}/** — Детали собаки.
- **PUT /api/v1/dogs/{dog_id}/** — Обновление собаки.
- **DELETE /api/v1/dogs/{dog_id}/** — Удаление собаки.

---

## Тестирование

Проект включает тесты, написанные с использованием **pytest**. Для запуска тестов выполните следующую команду:

```bash
docker exec -it django_dogs_ninja_web pytest
```

Тесты находятся в папке `tests/` и охватывают основные функции API, включая создание, чтение, обновление и удаление пород и собак.

---

## Структура проекта

```
django-dogs-ninja/
├── dogs_api/               # Основное приложение
├── tests/                  # Тесты
├── venv/                   # Виртуальное окружение
├── .env                    # Переменные окружения
├── .gitignore              # Игнорируемые файлы
├── docker-compose.yml      # Docker Compose
├── Dockerfile              # Dockerfile
├── manage.py               # Управление Django
├── pytest.ini              # Настройки pytest
├── README.md               # Документация
├── requirements.txt        # Зависимости
└── settings.py             # Настройки Django
```

---
