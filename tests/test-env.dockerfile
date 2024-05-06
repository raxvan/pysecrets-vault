FROM python:3.8

RUN apt-get update && apt-get install -y \
	cmake \
	git \
	nano

RUN pip3 install --upgrade pip && pip3 install \
	pudb

ENV VAULT_INSTALL_DIR=/repo
ENV VAULT_SERVER_SCALING=4

ENV VAULT_VERSION=0.0.1
ENV VAULT_HOST=0.0.0.0
ENV VAULT_PORT=5000
ENV VAULT_MAX_REQUEST_SIZE=1048576
ENV VAULT_CONFIG_DIR=/vault/config
ENV VAULT_DATA_DIR=/vault/data
ENV VAULT_SERVER_MODE=debug
ENV VAULT_PUBLISH_KEY=TRUE
ENV VAULT_STARTUP_TIME=2
