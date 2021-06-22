FROM nginx

ENV DEBIAN_FRONTEND noninteractive
ENV APT_KEY_DONT_WARN_ON_DANGEROUS_USAGE=DontWarn

RUN apt-get update && \
    apt-get install -y curl wget vim tcpdump net-tools iperf3 iptables traceroute bridge-utils ifupdown net-tools iputils-ping isc-dhcp-client traceroute && \
    rm -rf /var/lib/apt/lists/*

#ADD docker-entrypoint.sh /docker-entrypoint.sh
#RUN chmod +x /docker-entrypoint.sh
#ENTRYPOINT ["/docker-entrypoint.sh"]
