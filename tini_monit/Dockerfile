FROM ubuntu:18.04


RUN apt update && \
    apt install -y monit iproute2 iputils-ping net-tools vim sudo dos2unix && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

COPY files/monitrc /etc/monit/monitrc
COPY files/monit.conf /etc/monit/conf.d/monit.conf

# Add Tini
#ENV TINI_VERSION v0.18.0
#ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /tini
COPY files/tini /tini
RUN chmod +x /tini

COPY docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod +x /docker-entrypoint.sh

COPY files/rc.local /etc/rc.local
RUN chmod +x /etc/rc.local

ENTRYPOINT ["/tini", "--", "/docker-entrypoint.sh"]
