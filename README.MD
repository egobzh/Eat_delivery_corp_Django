# Корпоративная доставка еды
Сайт на котором можно заказать еду работникам компании.
## Описание
Небольшой PET-проект, делал его по ТЗ (прикреплено в репозитории) Техновизора. Реализовал весь функционал + доп. задания из раздела 'Факультативно' (все, кроме фронтенда на VueJS). Логин:пароль от админки admin:admin. 
## Технологии
* `Python`
* `Django`
* `Django ORM`
## Как запустить
1. Склонируйте репозиторий
2. Создайте и активируйте виртуальное окружение
```commandline 
python -m venv venv
GitBash: source venv/Scripts/activate
Windows: venv\Scripts\activate
Linux: source venv/bin/activate
```
3. Установите зависимости
```commandline 
pip install -r requirements.txt
```
4. Переместитесь в папку delivery из папки проекта.
```commandline 
GitBash: cd delivery
Windows: cd delivery
Linux: cd delivery
```
5. Запустите django приложение
```commandline 
python manage.py runserver
```