
auto eth0
iface eth0 inet static
	address 192.168.13.1
	netmask 255.255.255.0
	up /usr/bin/start_dhcp.sh 192.168.13.0/255.255.255.0:192.168.13.1

