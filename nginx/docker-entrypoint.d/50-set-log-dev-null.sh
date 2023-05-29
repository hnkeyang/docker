#!/bin/sh
#
sed -i 's#/var/log/nginx/access.log#/dev/null#g' /etc/nginx/nginx.conf
