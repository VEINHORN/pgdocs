FROM debian:latest

RUN apt-get update

RUN apt-get --assume-yes install postgresql-client-9.6

RUN apt-get --assume-yes install python3-pip

RUN pip3 install markdown2
RUN pip3 install pyyaml
RUN pip3 install xhtml2pdf

RUN apt-get --assume-yes install curl

COPY *.py /app/
COPY ./docker-entrypoint.sh /app/

RUN ["chmod", "+x", "/app/docker-entrypoint.sh"]

WORKDIR /app

ENTRYPOINT ["/app/docker-entrypoint.sh"]
