# A generic blueprint project for Django Rest Framework WIP

# Tech/framework used
### Built with 

![](https://img.shields.io/static/v1?label=Python&message=v3.7.x&color=lightgreen) ![](https://img.shields.io/static/v1?label=Django&message=v3.1.2&color=yellow)
![](https://img.shields.io/static/v1?label=DjangoRestFramework&message=v3.12.1&color=red) 
![](https://img.shields.io/static/v1?label=Docker&message=19.03.13&color=blue) ![](https://img.shields.io/static/v1?label=Docker-compose&message=1.27.4&color=blue) 
![](https://img.shields.io/static/v1?label=Flake8&message=3.8.4&color=green)
![](https://img.shields.io/static/v1?label=travis-ci&message=ci&color=red) 



 ### Uses docker and docker-compose
 https://docs.docker.com/get-docker/

## You have to setup your environment variables at .env.dev in the project root




# Quickstart
First clone the git repo or download it. 

# Time to build the images
## At the project's root folder
The argument "--env-file .env.dev " will inject the environment variables into container

# Run Atached to the console
```console
$ docker-compose --env-file .env.dev up
```
# Run Detached from console
```console
$ docker-compose --env-file .env.dev up -d
```
### To stop if attached
```console
ctrl+c to stop the process
```

### To stop if detached
```console
$ docker-compose down
```

# Endpoints:
- **/api/posts**
    - Allow: **GET, POST**
    - Content-Type: application/json
    - Also Django Rest Framework Interface
    - payload for **POST**
     ```javascript
    {
        "title": "What Stuff",
        "url": "https://margot.net"
    }
    ```

- **/api/posts/[int:id]**
    - Allow: **GET, PUT, PATCH, DELETE**
    - Content-Type: application/json
    - payload required only for **PATCH** or **PUT**
    - payload
     ```javascript
    {
        "title": "What Stuff",
        "url": "https://margot.net"
    }
    
- **/api/posts/[int:id]/vote**
    - Allow: **POST, DELETE**
    - Content-Type: application/json
    - DELETE returns code 204 no response
    - no payload required
    
- **/api/auth/signup**
    - Allow: **POST**
    - Content-Type: application/json
    - Returns token
    - payload     
    ```javascript
    {
       "username":"joao",
       "password":"secret"
    }
    ```
- **/auth/login**
    - Allow: **POST**
    - Content-Type: application/json
    - Returns token
    - payload
    ```javascript
    {
       "username":"joao",
       "password":"secret"
    }
    ```
### PS: Still work in progress