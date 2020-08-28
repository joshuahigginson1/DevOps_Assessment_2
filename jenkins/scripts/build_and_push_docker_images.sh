#!/bin/sh

# A script to build and push docker images to our personal repo.

docker login -u"$DOCKER_USERNAME" -p "$DOCKER_PASSWORD"

cd service1
docker build -t joshuahigginson1/melodie_service1:latest .
docker push joshuahigginson1/melodie_service1:latest

cd service2
docker build -t joshuahigginson1/melodie_service2:latest .
docker push joshuahigginson1/melodie_service2:latest

cd service3
docker build -t joshuahigginson1/melodie_service3:latest .
docker push joshuahigginson1/melodie_service3:latest

cd service4
docker build -t joshuahigginson1/melodie_service4:latest .
docker push joshuahigginson1/melodie_service4:latest


# Clean up images on Jenkins machine.

docker image prune -a -f