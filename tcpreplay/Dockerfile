FROM alpine
RUN apk update
RUN apk add bash
RUN apk add iputils
RUN apk add tcpdump
RUN apk add --no-cache iperf3 && adduser -S iperf
RUN apk add tcpreplay --repository=http://dl-cdn.alpinelinux.org/alpine/edge/testing/ --allow-untrusted
RUN apk add python3

ADD tcpreplay-ui /tcpreplay-ui

ADD docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod +x /docker-entrypoint.sh
ENTRYPOINT ["/docker-entrypoint.sh"]

