FROM python:3.6.6-stretch

# set working directory
WORKDIR /root

# copy requirements to container
COPY requirements.txt .

# install dependecies
RUN pip install -r requirements.txt
