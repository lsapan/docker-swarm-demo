FROM python:3.6-alpine

# Install python dependencies
COPY requirements.txt /home/docker/code/requirements.txt
RUN pip install -r /home/docker/code/requirements.txt

# Copy application code
COPY . /home/docker/code

WORKDIR /home/docker/code
