Установите Docker и docker-compose\
Установите ssl сертификаты letsencrypt\
Замените значение PRODUCTION_HOST на ваш домен в .env\
Запустите команду "docker-compose -f docker-compose.yml -f docker-compose.prod.yml up -d --build"\
Запустите команду "docker-compose -f docker-compose.yml -f docker-compose.prod.yml exec mans_leasing bash"
В открытом терминале докера запустите "./manage.py migrate", а затем "./manage.py collectstatic"
