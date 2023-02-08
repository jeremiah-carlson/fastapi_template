# syntax=docker/dockerfile:1
## Stage 1
FROM python:3.8.14-bullseye AS base
CMD /bin/bash
# Install openssl
RUN apt install openssl
# Install ODBC driver
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
RUN curl https://packages.microsoft.com/config/debian/11/prod.list > /etc/apt/sources.list.d/mssql-release.list
RUN apt update
RUN ACCEPT_EULA=Y apt-get install -y msodbcsql18

## Stage 2
FROM base
# Get app dir
COPY ./app /app
# Work in app dir
WORKDIR /app
# Upgrade pip
RUN /usr/local/bin/python -m pip install --upgrade pip
# Install requirements
RUN pip install -r /app/requirements.txt
# Run python script
ENTRYPOINT [ "python3" ]
CMD ["main.py"]