DOCKER_USERNAME=petermin123
DOCKER_IMAGE_NAME=project12

login:
	docker login -u ${DOCKER_USERNAME}

build:
	docker build -t ${DOCKER_IMAGE_NAME} .

run:
	docker run -p 5001:5000 -e FLASK_DEBUG=1 ${DOCKER_IMAGE_NAME}

show_local_images:
	docker images

show_running_containers:
	docker ps

push:
	docker login
	docker tag ${DOCKER_IMAGE_NAME} ${DOCKER_USERNAME}/${DOCKER_IMAGE_NAME}
	docker push ${DOCKER_USERNAME}/${DOCKER_IMAGE_NAME}:latest