FROM python:3.7-slim
# TODO Improve - change to alpine

# Installing packages
RUN apt update
RUN apt-get install -y python3-dev default-libmysqlclient-dev gcc
RUN rm -rf /var/lib/apt/lists/*

# Defining working directory and adding source code
WORKDIR /usr/src/app
COPY requirements.txt logging.conf  app.py reset_database.py ./

COPY instance/flask.cfg ./instance/flask.cfg

# Install API dependencies
RUN pip install -r requirements.txt

USER 1000
# Start app
CMD [ -f /usr/src/app/src/db.sqlite ] || python reset_database.py; flask run --host=0.0.0.0
