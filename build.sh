#!/bin/bash

cd packages
rm -f Dockerfile
echo "FROM $INSTANCE" >> Dockerfile
echo "WORKDIR /src" >> Dockerfile
echo "ENV DEBIAN_FRONTEND noninteractive" >> Dockerfile
echo "COPY test_script.sh /src" >> Dockerfile
echo "COPY test_script.sh /src" >> Dockerfile
echo "RUN chmod +x /src/test_script.sh" >> Dockerfile
echo "RUN /src/test_script.sh" >> Dockerfile
sudo iptables -L DOCKER || ( echo "DOCKER iptables chain missing" ; sudo iptables -N DOCKER )
python test_packages.py
docker build .
