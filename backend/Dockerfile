FROM python:3.8-slim
RUN apt-get update && apt-get install -y postgresql-client
WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:5000"]