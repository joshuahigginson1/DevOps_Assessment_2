#!/bin/sh

# A script to build and push docker images to our personal repo.

docker login -u"$DOCKER_USERNAME" -p "$DOCKER_PASSWORD"

cd service1
pwd
docker build -t joshuahigginson1/melodie_service1:latest .
docker push joshuahigginson1/melodie_service1:latest

cd ../service2
pwd
docker build -t joshuahigginson1/melodie_service2:latest .
docker push joshuahigginson1/melodie_service2:latest

cd ../service3
pwd
docker build -t joshuahigginson1/melodie_service3:latest .
docker push joshuahigginson1/melodie_service3:latest

cd ../service4
pwd
docker build -t joshuahigginson1/melodie_service4:latest .
docker push joshuahigginson1/melodie_service4:latest

cd ../nginx
pwd
docker build -t joshuahigginson1/melodie_nginx:latest .
docker push joshuahigginson1/melodie_nginx:latest


# Clean up images on Jenkins machine.

docker image prune -a -f