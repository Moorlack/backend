FROM python:3.11.3-slim-bullseye

COPY . /app
WORKDIR /app

RUN python -m pip install -r requirements.txt

CMD ["python", "run.py"]