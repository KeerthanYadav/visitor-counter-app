FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8080

CMD [ "REDIS_HOST=159.65.158.119", "REDIS_PORT=6379", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080" ]