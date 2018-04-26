# How to use it 

1. Build the docker image

        git clone https://github.com/stylesyou/sentiment-docker

        cd sentiment-docker
	
	`docker build -t sentiment:1.0 .`

2. Run the docker

  List the docker image build from previous step.

  	docker image list

  use the docker image id or name sentiment:1.0

	docker run -dti -p 80:80 --name sentiment sentiment:1.0

        docker ps 

	docker exec -it sentiment bash

4. copy the content if you need or just expose the port number

    copy code to files dir


