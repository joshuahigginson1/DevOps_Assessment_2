#!/bin/sh

# A script to build and push docker images to our personal repo.

docker login --username="$DOCKER_USERNAME" --password="$DOCKER_PASSWORD"

cd ~/DevOps_Assessment_2/service1
docker build -t joshuahigginson1/melodie_service1:latest
docker push joshuahigginson1/melodie_service1:latest

cd ~/DevOps_Assessment_2/service2
docker build -t joshuahigginson1/melodie_service2:latest
docker push joshuahigginson1/melodie_service2:latest

cd ~/DevOps_Assessment_2/service3
docker build -t joshuahigginson1/melodie_service3:latest
docker push joshuahigginson1/melodie_service3:latest

cd ~/DevOps_Assessment_2/service4
docker build -t joshuahigginson1/melodie_service4:latest
docker push joshuahigginson1/melodie_service4:latest