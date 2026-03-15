# Развёртывание на VPS (Ubuntu)

Краткая инструкция по деплою Django-сайта на сервер с Nginx и gunicorn.

## Предполагаемая среда

- Ubuntu 20.04 / 22.04
- Python 3.10+ (установлен системно или через pyenv)
- Для продакшена рекомендуется PostgreSQL; для минимального хостинга можно оставить SQLite.

## 1. Подготовка сервера

```bash
sudo apt update
sudo apt install -y python3-venv python3-pip nginx
# При использовании PostgreSQL:
# sudo apt install -y postgresql libpq-dev
```

## 2. Размещение проекта

```bash
cd /var/www  # или другой каталог
sudo git clone <URL_РЕПОЗИТОРИЯ> axelot-site
cd axelot-site
sudo chown -R $USER:$USER .
```

## 3. Окружение и зависимости

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## 4. Переменные окружения

```bash
cp .env.example .env
nano .env
```

Указать:
- `SECRET_KEY` — уникальный секретный ключ (например, сгенерировать: `python -c "import secrets; print(secrets.token_urlsafe(50))"`)
- `DEBUG=False`
- `ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com,IP_СЕРВЕРА`
- При PostgreSQL: `DATABASE_URL=postgresql://user:password@localhost:5432/dbname`

## 5. Миграции и статика

```bash
source venv/bin/activate
python manage.py migrate
python manage.py createsuperuser
python manage.py collectstatic --noinput
```

## 6. Gunicorn (systemd)

Создать unit-файл `/etc/systemd/system/axelot.service`:

```ini
[Unit]
Description=Axelot Django site (gunicorn)
After=network.target

[Service]
User=www-data
Group=www-data
WorkingDirectory=/var/www/axelot-site
Environment="PATH=/var/www/axelot-site/venv/bin"
ExecStart=/var/www/axelot-site/venv/bin/gunicorn --workers 3 --bind unix:/var/www/axelot-site/axelot.sock config.wsgi:application
Restart=on-failure

[Install]
WantedBy=multi-user.target
```

Подставить свой каталог и пользователя. Запуск:

```bash
sudo systemctl daemon-reload
sudo systemctl enable axelot
sudo systemctl start axelot
sudo systemctl status axelot
```

## 7. Nginx

Пример конфигурации `/etc/nginx/sites-available/axelot`:

```nginx
server {
    listen 80;
    server_name yourdomain.com www.yourdomain.com;

    location = /favicon.ico { access_log off; log_not_found off; }

    location /static/ {
        alias /var/www/axelot-site/staticfiles/;
    }

    location /media/ {
        alias /var/www/axelot-site/media/;
    }

    location / {
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_pass http://unix:/var/www/axelot-site/axelot.sock;
    }
}
```

Включить сайт и перезапустить Nginx:

```bash
sudo ln -s /etc/nginx/sites-available/axelot /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl reload nginx
```

Для HTTPS настроить SSL (например, certbot с Let's Encrypt).

## 8. Проверка

- Открыть в браузере http://yourdomain.com
- Проверить отправку формы заявки и появление записи в админке: http://yourdomain.com/admin/
