# pull official base image
FROM python:3.7-alpine
LABEL JXTECH ltd.
# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apk add --update --no-cache postgresql-client
RUN apk add --update --no-cache --virtual .tmp-build-deps gcc \ 
libc-dev linux-headers postgresql-dev musl-dev dos2unix
# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt
RUN apk del .tmp-build-deps

# copy entrypoints
COPY ./entrypoint.sh .
COPY ./check-pgsql.py .
# copy project
COPY . .
RUN dos2unix ./entrypoint.sh

# run entrypoint.sh
ENTRYPOINT ["sh","/usr/src/app/entrypoint.sh"]
