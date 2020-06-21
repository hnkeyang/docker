#!/bin/sh
#

cat - > /etc/dhcp/dhcpd.conf <<\EOF
ddns-update-style interim;
ignore client-updates;
authourtative;
default-lease-time 36000;
max-lease-time 360000;

EOF

for args in $*;do
subnet=${args%/*}
netmask=${args##*/}
netmask=${netmask%:*}

gateway=${args#*:}
[ -z "$gateway" ] && gateway=${subnet%.0}.1

cat - <<EOF
subnet $subnet netmask $netmask {
  option routers $gateway; 
  option domain-name-servers 114.114.114.114; 
  option domain-name "test.com";

  range ${args%.0/*}.100 ${args%.0/*}.200;

}
EOF
done >> /etc/dhcp/dhcpd.conf
