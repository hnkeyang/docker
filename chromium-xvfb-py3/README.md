# chromium-xvfb-py3

## get website response time

## response time
root@hm01:~# docker run -e URL=https://www.google.com -v /opt:/opt --rm hnkeyang/chromium-xvfb-py3
1913

## website screenshot
root@hm01:~# ls -al /opt/screenshot.png 
-rw-r--r-- 1 root root 51706 Dec 12 15:08 /opt/screenshot.png
