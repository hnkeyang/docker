FROM ubuntu:18.04
MAINTAINER hnkeyang@gmail.com
RUN apt-get update && \
    apt-get install -y libpcre3-dev apt-transport-https ca-certificates curl wget logrotate \
    libc-ares2 libjson-c3 vim systemd procps apt-utils sed iproute2 iputils-ping traceroute
RUN curl -sLO https://deb.frrouting.org/frr/pool/frr-stable/liby/libyang/libyang0.16_0.16.105-1~ubuntu18.04.1_amd64.deb && dpkg -i libyang0.16_0.16.105-1~ubuntu18.04.1_amd64.deb && \
    curl -sLO https://deb.frrouting.org/frr/pool/frr-stable/f/frr/frr_7.0-1~ubuntu18.04.1_amd64.deb && dpkg -i frr_7.0-1~ubuntu18.04.1_amd64.deb && \
    sed -i '/^bgpd=/s/no/yes/g;/^ospfd=/s/no/yes/g;/^pbrd=/s/no/yes/g' /etc/frr/daemons
ADD docker-start /usr/sbin/docker-start
ENTRYPOINT ["/usr/sbin/docker-start"]
