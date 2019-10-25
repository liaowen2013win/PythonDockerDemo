FROM centos:7
MAINTAINER REGAN liaowen2013win@163.com
#ADD centos-7-docker.tar.xz /
#LABEL org.label-schema.schema-version="1.0" \
#    org.label-schema.name="CentOS Base Image" \
#    org.label-schema.vendor="CentOS" \
#    org.label-schema.license="GPLv2" \
#    org.label-schema.build-date="20181204"
RUN yum update -y && \
    yum install -y python3-pip python3-dev
COPY ./requirements.txt /requirements.txt
WORKDIR /
RUN pip3 install -r requirements.txt
COPY . /
ENTRYPOINT [ "python3" ]
CMD [ "app/app.py","--port=9999" ]

### docker build -t docker-tonado:0.1 .
### docker run -d --name docker_tonado_app -v $PWD/app:/app -p 9999:9999 docker-tonado:0.1