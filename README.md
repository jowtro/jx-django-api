# A generic blueprint project for Django Rest Framework WIP


 ### docker and docker-compose

## You have to setup your environment variables at .env.dev in the project root

# create this file in project's root ".env.dev"
```console
DEBUG=True
SECRET_KEY=GENERATE YOURS HERE https://djecrety.ir/
DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1]
SQL_ENGINE=django.db.backends.postgresql_psycopg2
POSTGRES_DB=zappit
POSTGRES_USER=postgres
POSTGRES_PASSWORD=123qwe.
SQL_HOST=db
SQL_PORT=5432
DATABASE=zappit
```
## tip --env-file will load the file to environment variables
## to run you need the following command
```console
use bellow
# first time to build the images
$ docker-compose --env-file .env.dev up --build
# to start the containers
$ docker-compose --env-file .env.dev up
OR
$ ./start-app-dev.sh #TODO
```






# Tech/framework used
### Built with 

![](https://img.shields.io/static/v1?label=Python&message=v3.7.x&color=lightgreen) ![](https://img.shields.io/static/v1?label=Django&message=v3.1.2&color=yellow)
![](https://img.shields.io/static/v1?label=DjangoRestFramework&message=v3.12.1&color=red) 
![](https://img.shields.io/static/v1?label=Docker&message=19.03.13&color=blue) ![](https://img.shields.io/static/v1?label=Docker-compose&message=1.27.4&color=blue) 
![](https://img.shields.io/static/v1?label=Flake8&message=3.8.4&color=green)
![](https://img.shields.io/static/v1?label=travis-ci&message=ci&color=red) 

# API Reference
### todo

