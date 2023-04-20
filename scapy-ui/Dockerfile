FROM alpine
RUN apk update
RUN apk add bash
RUN apk add iputils
RUN apk add tcpdump
RUN apk add python3
RUN apk add ipython
RUN apk add scapy

ADD scapy-ui /scapy-ui

ADD docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod +x /docker-entrypoint.sh
ENTRYPOINT ["/docker-entrypoint.sh"]

