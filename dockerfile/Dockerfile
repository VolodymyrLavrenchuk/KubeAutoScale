# © 2018 Quest Inc.
# ALL RIGHTS RESERVED.
#
# Kubernates Nodes Autoscaler Dockerfile
#

FROM python:3.6-alpine

RUN apk add --no-cache vim build-base libffi-dev openssl-dev
RUN pip install requests retrying docker azure-mgmt-containerservice

COPY ./pkg /scripts/pkg
COPY ./worker.py /scripts/worker.py
WORKDIR /scripts

ARG GIT_STATUS
ARG GIT_COMMIT
ARG IMAGE_TAG

ENV GIT_STATUS $GIT_STATUS
ENV GIT_COMMIT $GIT_COMMIT
ENV IMAGE_TAG $IMAGE_TAG

ENTRYPOINT [ "python", "./worker.py" ]