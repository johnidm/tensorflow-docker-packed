DOCKER_IMAGE_NAME = "iara-ml"


install-dependences: 
	pip install -r requirements-dev.txt
	
jupyter-notebook:
	jupyter notebook notebooks

docker-run:
	docker build  -t ${DOCKER_IMAGE_NAME}:master .
	docker run  -p 8000:8000 ${DOCKER_IMAGE_NAME}:master

test-run:
	pytest