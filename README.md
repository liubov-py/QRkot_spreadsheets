# Приложение для Благотворительного фонда поддержки котиков QRKot

Фонд собирает пожертвования на различные целевые проекты: на медицинское обслуживание нуждающихся хвостатых, на обустройство кошачьей колонии в подвале, на корм оставшимся без попечения кошкам — на любые цели, связанные с поддержкой кошачьей популяции.


## Запуск проекта
### Установить и активировать виртуальное окружение
python -m venv venv
source venv/Scripts/activate

### Установить список зависимостей Requirements.txt
pip install -r requirements.txt

### Применить миграции
alembic upgrade head

### Запусить проект:
uvicorn app.main:app --reload


## Примеры запросов:
### Get All Charity Projects
Возвращает список всех проектов.
GET
/charity_project

Ответ:
[
{
"name": "string",
"description": "string",
"full_amount": 0,
"id": 0,
"invested_amount": 0,
"fully_invested": true,
"create_date": "2019-08-24T14:15:22Z",
"close_date": "2019-08-24T14:15:22Z"
}
]

### Create Charity Project
Только для суперюзеров.

Создаёт благотворительный проект.
POST
/charity_project
{
"name": "string",
"description": "string",
"full_amount": 0
}

Ответ:
{
"name": "string",
"description": "string",
"full_amount": 0,
"id": 0,
"invested_amount": 0,
"fully_invested": true,
"create_date": "2019-08-24T14:15:22Z",
"close_date": "2019-08-24T14:15:22Z"
}


### Create Donation
Сделать пожертвование.

POST
/donation
{
"full_amount": 0,
"comment": "string"
}

Ответ:
{
"full_amount": 0,
"comment": "string",
"id": 0,
"create_date": "2019-08-24T14:15:22Z"
}


