# Use Python slim-buster as the base image
FROM python:3.13-slim-bullseye

# Set non-interactive mode for installation
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y git

# Get latest version of pip
RUN pip install --upgrade pip 

# copy requirements.txt to working directory, install, upgrade dependencies & remove the file
COPY requirements.txt .
RUN pip install --upgrade -r requirements.txt 
RUN rm requirements.txt


#Clean Up
RUN apt-get clean \
    && rm -rf /var/lib/apt/lists/*