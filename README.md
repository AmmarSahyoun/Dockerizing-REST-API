# Dockerizing-REST-API

Create a docker image by docker file then instantiate a runtime container

* module 1: simple flask_API
> ####docker build -t productservice . 
> ####docker run -d -p 5000:5000 productservice
> ####docker ps