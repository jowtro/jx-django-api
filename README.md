# A generic blueprint project for Django Rest Framework WIP


 ### Uses docker and docker-compose

## You have to setup your environment variables at .env.dev in the project root




### Quickstart

# First time building the images and running
```console
$ docker-compose --env-file .env.dev up --build
```

# docker-compose cheatsheet

### To start the containers
The arg "--env-file .env.dev " will inject the environment variables into container
```console
$ docker-compose --env-file .env.dev up
```

### To stop
```console
$ docker-compose down
```

### To stop and remove volumes  -v, Remove named volumes declared in the `volumes`
```console
$ docker-compose down -v
```






# Tech/framework used
### Built with 

![](https://img.shields.io/static/v1?label=Python&message=v3.7.x&color=lightgreen) ![](https://img.shields.io/static/v1?label=Django&message=v3.1.2&color=yellow)
![](https://img.shields.io/static/v1?label=DjangoRestFramework&message=v3.12.1&color=red) 
![](https://img.shields.io/static/v1?label=Docker&message=19.03.13&color=blue) ![](https://img.shields.io/static/v1?label=Docker-compose&message=1.27.4&color=blue) 
![](https://img.shields.io/static/v1?label=Flake8&message=3.8.4&color=green)
![](https://img.shields.io/static/v1?label=travis-ci&message=ci&color=red) 
