FROM nginx

ENV DEBIAN_FRONTEND noninteractive
ENV APT_KEY_DONT_WARN_ON_DANGEROUS_USAGE=DontWarn

RUN apt-get update && \
    apt-get install -y curl wget vim tcpdump net-tools iperf3 iptables traceroute bridge-utils ifupdown net-tools iproute2 iputils-ping isc-dhcp-client traceroute procps && \
    rm -rf /var/lib/apt/lists/*


COPY docker-entrypoint.d/40-set-worker-processes.sh /docker-entrypoint.d/
RUN chmod +x /docker-entrypoint.d/40-set-worker-processes.sh

COPY docker-entrypoint.d/50-set-log-dev-null.sh /docker-entrypoint.d/
RUN chmod +x /docker-entrypoint.d/50-set-log-dev-null.sh

