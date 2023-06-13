FROM alpine:3.17

RUN apk update && apk add --no-cache \
  tini monit bash \
  openconnect gnutls-utils \
  tcpdump busybox-extras curl iputils traceroute


COPY docker-entrypoint.sh /
RUN chmod +x /docker-entrypoint.sh

COPY openconnect_start.sh /
RUN chmod +x /openconnect_start.sh

COPY monitrc /etc/
COPY openconnect_monit.conf /etc/monit.d/

#ENTRYPOINT ["/docker-entrypoint.sh"]
ENTRYPOINT ["/sbin/tini", "--", "/docker-entrypoint.sh"]
