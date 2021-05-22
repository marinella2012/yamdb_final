# Проект YaMDb
[![Yamdb-app workflow](https://github.com/marinella2012/yamdb_final/workflows/yamdb_workflow.yml/badge.svg)](https://github.com/marinella2012/yamdb_final/actions)

REST API для сервиса YaMDb — базы отзывов о фильмах, книгах и музыке. (Совместный проект группы из 3 студентов Яндекс.Практикум)


## Технологический стек


- [Python 3.8](https://www.python.org/downloads/)
- [Django 3](https://www.djangoproject.com/start/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [Simple JWT](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/getting_started.html) - работа с токеном
- [Django-filter](https://django-filter.readthedocs.io/en/stable/guide/install.html) - фильтрация запросов
- [PostgreSQL](https://www.postgresql.org/download/) - база данных



## Установка

Необходим установленный и запущенный Docker.
Инструкция по установке см. [Docker](https://www.docker.com/get-started#h_installation).

## Первый запуск проекта

Клонирование репозитория
```
git clone https://github.com/marinella2012/infra_sp2.git
```
Сборка и запуск образа
```
docker-compose up -d --build
```
При первом запуске для функционирования проекта необходимо создать и выполнить миграции
```
docker-compose exec web python manage.py makemigrations
docker-compose exec web python manage.py migrate
```
Сбор статики
```
docker-compose exec web python manage.py collectstatic
```
Создание учетной записи администратора
```
docker-compose exec web python manage.py createsuperuser
```
Загрузка в базу тестовых данных
```
docker-compose exec web python manage.py loaddata fixtures.json
```
Регулярный запуск
```
docker-compose up -d
```
Перейти в документацию API ([redoc.yaml](https://github.com/marinella2012/infra_sp2/blob/master/static/redoc.yaml)) 
```
http://127.0.0.1:8000/redoc/
```
