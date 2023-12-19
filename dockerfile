FROM python:3.11.3-slim-bullseye

WORKDIR /app
COPY requirements.txt .

RUN python -m pip install -r requirements.txt

COPY . /app

EXPOSE 5000

CMD ["flask", "run", "--host", "0.0.0.0", "-p", "5000"]