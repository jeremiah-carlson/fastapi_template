#!/bin/bash
docker build -t api_template . &&\
docker run \
--name api_template \
--restart unless-stopped \
-d -p 8080:8080 -p 443:443 api_template