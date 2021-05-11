FROM ubuntu:18.04

RUN apt-get update && \
    apt-get install -y \
    iproute2 net-tools isc-dhcp-client ifupdown \
    iputils-ping bridge-utils tcpdump iperf iperf3 \
    vim mtr socat curl wget dnsutils netcat-openbsd telnet openssh-client openssh-server rsync \
    apache2 nginx \
    && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*
