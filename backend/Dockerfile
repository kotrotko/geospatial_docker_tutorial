FROM python:3.9
WORKDIR /app
COPY backend /app/backend/
COPY manage.py requirements.txt /app/
RUN pip install -r requirements.txt
EXPOSE 8000
