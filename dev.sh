docker run --name mysql -d -p 3306:3306 -e MYSQL_ROOT_PASSWORD=root mysql:8
docker run -d -p 6379:6379 redis

create database mps_dev character set utf8mb4 collate utf8mb4_general_ci;

pip freeze > requirements.txt

# on windows, need `-P threads`
celery -A rtc_ai worker -l info -P threads
celery -A rtc_ai beat -l info
python3 manage.py runserver 0.0.0.0:8000