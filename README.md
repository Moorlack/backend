# My Backend Labs on Python/Flask

### Виконав: Васютинський Олександр IO-13

## Deploy
http://194.183.165.223:4445

## Postman
https://www.postman.com/moorlack/workspace/kpi-backend

## Installation

### Run dev server:
 - Install Python and pip
 - Install dependencies
 ```shell
pip install -r requirements.txt
 ```
 - Make migrations
 - Run server
 ```shell  
python run.py
 ```

### Run prod server:
 - Make configuration in docker-compose.yaml (Db url, jwt secret key, port, ...)
 - Run build and starting of container
```shell
docker compose up --build
```

### Migrations
You must migrate database to make app working correctly

If you use project docker configuration, you can access container via 
```shell
docker compose exec -it <api_container_name> bash
```
Run this commands
```shell
flask --app run db init
flask --app run db migrate
flask --app run db upgrade
```