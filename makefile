all: build run

build:
	sudo docker build -t http .

run:
	sudo docker run --rm -p 8080:8080 -d http
