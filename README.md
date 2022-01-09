Десять песен
=
Это моя домашняя работа на новогодние каникулы для Elbrus Bootcamp

>Проект вдохновлен и построен вокруг https://github.com/Atienon/flask-styl
## Описание
Десять песен - Маленький сервис музыкальных рекомендаций на основе Spotify API. Пользователь пишет название песни в бота или веб интерфейс и получает 10 рекомендаций

## Cтруктура
Проект состоит из трех компонентов:
| | |
|-----|-------|
|Веб интерфейс| Flask|
|Веб api |Fast Api
|Телегамм бот|  Aiogram|


## Запуск проекта

1) Клонируйте репозиторий
   ```
   git clone https://github.com/andystep1/Project_holiday
   ```
2) **bot/config.py** вставьте токен своего бота в телеграмм
3) **docker-compose.yml** для flask и fast api задайте следующие переменные среды:
    >SPOTIPY_CLIENT_ID - id вашего приложения

    >SPOTIPY_CLIENT_SECRET - его секрет

    >SECRET_KEY - может быть любой строкой
4) ```bash
   docker-compose up
   ```