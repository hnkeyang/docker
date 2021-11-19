#!/bin/sh

##
# For volume mounts...
##
brctl addbr br0
brctl addif br0 eth0
brctl addif br0 eth1
ip link set br0 up
ip link set eth0 up
ip link set eth1 up

service apache2 restart

exec sleep 365d
