# Peter_Min_Data_Engineering_Project12
[![CI/CD Pipeline](https://github.com/nogibjj/Peter_Min_Data_Engineering_Project12/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/Peter_Min_Data_Engineering_Project12/actions/workflows/cicd.yml)


This is the README for my Mini Project 12, Dockerized Python Applications for the IDS706 - Data Engineering Systems class at Duke University.

## Overview
The idea of this project is to gain an understanding of common Docker commands and apply Docker to package an existing Flask-based Python application and push it to DockerHub remotely.

## To use this project:
- Clone this repo using `git clone ...`
- Ensure you have downloaded Docker and it is running.
- Run `make build`. The underlying command will build a Docker image of the code and the app.
- Run `make run`.
- Navigate to the first URL provided and use port number 5001 (e.g. http://127.0.0.1:5000)
- Use the endpoint `/random_cs_jokes` and you will see a random computer science joke being shown to you.

## Link to Docker Image
https://hub.docker.com/repository/docker/petermin123/project12/general
