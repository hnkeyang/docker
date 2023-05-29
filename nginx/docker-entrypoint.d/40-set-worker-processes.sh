#!/bin/sh
#

ncpu=${NGINX_WORK_PROCESS:-4}
sed -i.bak -r 's/^(worker_processes)(.*)$/\1 '"$ncpu"';/' /etc/nginx/nginx.conf
