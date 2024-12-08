# Peter_Min_Data_Engineering_Individual_Project_3
[![CI/CD Pipeline](https://github.com/nogibjj/Peter_Min_Data_Engineering_Individual_Project3/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/Peter_Min_Data_Engineering_Individual_Project3/actions/workflows/cicd.yml)


This is the README for my Individual Project 3, which is about building a publicly accessible auto-scaling container using AWS Services and Flask app for the IDS706 - Data Engineering Systems class at Duke University.

## Overview
The idea of this project is to package an existing Flask app using Docker and using AWS to host the Docker image and make it publicly accessible using AWS ECR and AWS App Runner for auto-scaling feature.

For my Flask app, I integrated [Jokes API](https://sv443.net/jokeapi/v2/) with a LLM supported by (Groq)[https://console.groq.com/docs/overview]. When a user clicks the button, it will generate a random CS/programming-related joke and ask Llama to explain the joke to them.

## Local Flask Run
![alt text](./assets/local_flask_run.png)
