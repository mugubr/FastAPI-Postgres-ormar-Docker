FROM python:latest
COPY requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt
COPY . /app
WORKDIR /app
EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
ENV POSTGRES_USER=fastapi_user
ENV POSTGRES_PASSWORD=password
ENV POSTGRES_DB=fastapi_database
ENV POSTGRES_HOST=db
ENV POSTGRES_PORT=5432