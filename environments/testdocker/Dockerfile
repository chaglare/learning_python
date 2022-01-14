# Docker file for a slim Ubuntu-based Python3 image

FROM debian
MAINTAINER fnndsc "dev@babymri.org"

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update \
  && apt-get install -y python3-pip python3-dev python3-apt python3-twisted curl \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 --no-cache-dir install --upgrade pip \
  && rm -rf /var/lib/apt/lists/* \
  && apt-get clean

RUN pip3 install -U pip

RUN apt-get update
RUN apt-get install -y docker.io