## Начало работы:

* Клонируйте репозиторий `bewise_test`
```bash
git clone https://github.com/pichugina-v/bewise_test.git
```

* Перейдите в директорию `webapp` и установите зависимости
```bash
cd webapp/
pip3 install -r requirements.txt
```

* В директории `webapp` проекта создайте файл `.env` и заполните переменные окружения
```python
POSTGRES_DB=quiz
POSTGRES_USER=<логин для подключения к базе данных> (quiz_user)
POSTGRES_PASSWORD=<пароль для подключения к базе данных> (5372)
POSTGRES_PORT=5432
POSTGRES_HOST=db
```

* В директории `webapp` проекта создайте файл `.flaskenv` и заполните переменные окружения
```python
FLASK_APP=__init__
```

* Из директории `webapp` запустите `docker-compose` командой 
```bash
sudo docker-compose up -d --build
```

* Примените миграции
```bash
sudo docker-compose exec web flask db upgrade
```

# Примеры использования:
* Для создания нового поста отправьте POST-запрос на адрес http://127.0.0.1:5000/api/. В запросе обязательно передать
```python
questions_num: <integer>
```

* Примеры ответа:
```python
{
    "question": "The most recent of these devices can achieve accuracy to within about 1 second in every 3 million years"
}
```
```python
{
    "error_message": "Value must be greater than 0"
}
```