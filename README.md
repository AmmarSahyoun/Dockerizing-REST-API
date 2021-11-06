# Dockerizing-REST-API

Create a docker image by docker file then instantiate a runtime container

> module 1: simple flask_API
* docker build -t productservice . 
* docker run -d -p 5000:5000 productservice
* docker ps

> module 2: Multi-container by docker compose, YAML config and Nginx container, MySQL container
* docker-compose build 
* docker-compose up -d
* Test end-to-end
* docker-compose down

> Test container application
* Create collection test in Postman