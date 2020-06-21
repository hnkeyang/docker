FROM gns3/endhost

RUN chmod +x /bin/start-ssh.sh
RUN apk add tcpdump
RUN apk add apache2
RUN apk add --no-cache iperf3 && adduser -S iperf
COPY start-apache.sh /bin/start-apache.sh
RUN chmod +x /bin/start-apache.sh
RUN apk add tmux
