#!/bin/bash
#
[ -x /etc/rc.local ] && /etc/rc.local

exec /usr/bin/monit
