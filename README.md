# test_task
Тестовое задание для вакансии "Python-разработчик" от компании HR365

## Задание 
Написать сервис "Конвертер валют" который работает по REST-API

## Описание проекта 
По GET запросу к адресу `localhost/api/rates/from=<ПерваяВалюта>&to=<ВтораяВалюта>&value=<количество>` приложение возвращает конвертированную сумму

Проект можно тестировать через swagger и postman

В качестве API для получения курса валют использовано `https://currate.ru`

## Стек 

- Python 3.9
- Django REST framework
- API

## Запуcк проекта: 

1) Клонировать репозиторий и перейти в него в командной строке:
git@github.com:sic15/test_task_HR365.git

2) Перейти в папку catalog:
cd test_task_HR365/HR_365/

3) Cоздать и активировать виртуальное окружение:
python -m venv venv 
source venv/scripts/activate

4) Установить зависимости из файла requirements.txt:
python -m pip install --upgrade pip pip install -r requirements.txt

5) Выполнить миграции:
python manage.py migrate

6) Запустить проект:
python manage.py runserver

## Об авторе 
Автор проекта Наталья Арлазарова
