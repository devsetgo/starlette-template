#!/bin/bash
set -e
set -x

# cat /home/mike/twitter-star/app/scripts/docker_token.txt | docker login docker.pkg.github.com -u devsetgo --password-stdin

IMAGE_NAME="pynoteii"
IMAGE_VERSION=$(TZ=America/New_York date +"%y-%m-%d")

docker build -t docker.pkg.github.com/devsetgo/pynote_ii/$IMAGE_NAME:$IMAGE_VERSION-rc .
docker push docker.pkg.github.com/devsetgo/pynote_ii/$IMAGE_NAME:$IMAGE_VERSION-rc