#!/bin/sh

# A script to build and push docker images to our personal repo.

docker login -u"$DOCKER_USERNAME" -p "$DOCKER_PASSWORD"

pwd
ls

sudo cd ~/DevOps_Assessment_2/service1
docker build -t joshuahigginson1/melodie_service1:latest .
docker push joshuahigginson1/melodie_service1:latest

sudo cd ~/DevOps_Assessment_2/service2
docker build -t joshuahigginson1/melodie_service2:latest .
docker push joshuahigginson1/melodie_service2:latest

sudo cd ~/DevOps_Assessment_2/service3
docker build -t joshuahigginson1/melodie_service3:latest .
docker push joshuahigginson1/melodie_service3:latest

sudo cd ~/DevOps_Assessment_2/service4
docker build -t joshuahigginson1/melodie_service4:latest .
docker push joshuahigginson1/melodie_service4:latest