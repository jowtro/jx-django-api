FROM python:3.7-alpine
LABEL JXTECH ltd.

ENV PYTHONUNBUFFERED 1

# Copy requirements file to container
COPY ./requirements.txt /requirements.txt

# install postgresql client
RUN apk add --update --no-cache postgresql-client
# install postgresql client dependencies
RUN apk add --update --no-cache --virtual .tmp-build-deps gcc libc-dev linux-headers postgresql-dev
RUN pip install --upgrade pip
# install dependencies 
RUN pip install -r /requirements.txt
# delete temp folder
RUN apk del .tmp-build-deps

# Setup directory structure in container
RUN mkdir /app
# set workdir where all commands are executed
WORKDIR /app


# add user to the process so it can't run as root
RUN adduser -D user
USER user

# copy project
COPY ./app/ /app
# run entrypoint.sh basicaly to wait the postgresql to run and execute python
# commands
ENTRYPOINT ["/app/entrypoint.sh"]