FROM ubuntu:devel
RUN apt update --yes
RUN apt install --yes python3
COPY . src
WORKDIR src
CMD ./serve.py
