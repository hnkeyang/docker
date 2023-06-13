#!/bin/sh
#

#VPN_SERVER=192.168.1.1:1443
#VPN_LOGIN=user
#VPN_PASSWORD=pass

SERVERCERT=$(timeout 1 gnutls-cli --insecure $VPN_SERVER |awk '/\tsha256:/{print $0}')
echo $VPN_PASSWORD |openconnect -u $VPN_LOGIN --pid-file=/var/run/openconnect.pid --servercert $SERVERCERT $VPN_SERVER --passwd-on-stdin -b
