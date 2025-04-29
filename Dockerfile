# Use Python slim-buster as the base image
FROM python:3.13-slim-bullseye

# Set non-interactive mode for installation
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y git

# Install Fish and set as default shell
RUN apt-get update && apt-get install -y fish && \
    echo $(which fish) >> /etc/shells && \
    chsh -s $(which fish)

# Set Fish as default for the 'vscode' user (if using)
RUN if id root &>/dev/null; then \
      chsh -s $(which fish) root; \
    fi

# Get latest version of pip
RUN pip install --upgrade pip 

# copy requirements.txt to working directory, install, upgrade dependencies & remove the file
COPY requirements.txt .
RUN pip install --upgrade -r requirements.txt 
RUN rm requirements.txt


#Clean Up
RUN apt-get clean \
    && rm -rf /var/lib/apt/lists/*