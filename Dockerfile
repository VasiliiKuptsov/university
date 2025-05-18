FROM python:3.11-slim

WORKDIR /code

COPY ./requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .
# создаем права на дирректорию для статич файлов
RUN mkdir -p /app/staticfailes && chmod -R 755 /app/stativfiles

EXPOSE 8000

CMD ["sh", "-c", "python manage.py collectstatic --noinput && gunicorn config.wsgi.application --bind 0.0.0.0:8000"]