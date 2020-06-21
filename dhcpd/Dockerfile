FROM alpine:latest

RUN apk add --no-cache dhcp monit

RUN touch /var/lib/dhcp/dhcpd.leases
COPY dhcpd.conf  /etc/dhcp/dhcpd.conf

RUN mkdir /etc/monit.d
COPY monitrc /etc/
COPY dhcpd.monit /etc/monit.d/

COPY start_dhcp.sh /usr/bin/
RUN chmod +x /usr/bin/start_dhcp.sh

COPY dumb-init_1.2.2_amd64 /usr/bin/dumb-init

CMD ["/usr/bin/dumb-init", "--", "/usr/bin/monit", "-I"]
