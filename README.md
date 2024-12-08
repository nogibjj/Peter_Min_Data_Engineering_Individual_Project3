# Peter_Min_Data_Engineering_Individual_Project_3
[![CI/CD Pipeline](https://github.com/nogibjj/Peter_Min_Data_Engineering_Individual_Project3/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/Peter_Min_Data_Engineering_Individual_Project3/actions/workflows/cicd.yml)

[Demo Video on YouTube](https://youtu.be/85bLv4lr9Bs)
&nbsp;&nbsp;![YouTube Video Views](https://img.shields.io/youtube/views/85bLv4lr9Bs)


This is the README for my Individual Project 3, which is about building a publicly accessible auto-scaling container using AWS Services and Flask app for the IDS706 - Data Engineering Systems class at Duke University.

## Overview
The idea of this project is to package an existing Flask app using Docker and using AWS to host the Docker image and make it publicly accessible using AWS ECR and AWS App Runner for auto-scaling feature.

For my Flask app, I integrated [Jokes API](https://sv443.net/jokeapi/v2/) with a LLM supported by (Groq)[https://console.groq.com/docs/overview]. When a user clicks the button, it will generate a random CS/programming-related joke and ask Llama to explain the joke to them.

To use the publicly-accessible app hosted by AWS, please visit [this link](https://3sybanupbh.us-east-2.awsapprunner.com/).

## Local Flask Run
![alt text](./assets/local_flask_run.png)

## AWS App Runner Deployment
![alt text](./assets/aws_app_runner_deployment.png)

## AWS-hosted Domain Access
![alt text](./assets/app_from_aws_domain.png)
