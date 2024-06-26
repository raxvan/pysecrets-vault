FROM python:3.8

RUN apt-get update && apt-get install -y \
	cmake \
	git \
	nano

RUN pip3 install --upgrade pip && pip3 install \
	pudb \
	cryptography \
	requests \
	flask \
	gunicorn \
	netifaces \
	shared-memory-dict

ENV VAULT_INSTALL_DIR=/repo

ENV VAULT_HOST=0.0.0.0
ENV VAULT_PORT=5000
ENV VAULT_MAX_REQUEST_SIZE=1048576
ENV VAULT_CONFIG_DIR=/vault/config
ENV VAULT_DATA_DIR=/vault/data
ENV VAULT_LOGS_DIR=/vault/logs
ENV VAULT_SERVER_MODE=debug
ENV VAULT_PUBLIC_ACCESS=enable
