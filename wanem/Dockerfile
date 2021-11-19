FROM debian:8

RUN apt-get update && \
    apt-get -y install net-tools vim git sudo bridge-utils tcpdump && \
    apt-get -y install apache2 php5 libapache2-mod-php5
RUN git clone https://github.com/worryboy/WANem.git
RUN rsync -avg WANem/var/www/ /var/www/ && \
    rsync -avg WANem/etc/ /etc/ && \
    rsync -avg WANem/root/ /root/

RUN line_number_443=$(grep -n :443 /etc/apache2/sites-available/000-default.conf |awk -F ":" '{print $1;exit}') && \
    sed "$line_number_443"',$d;/ProxyPass/d' -i /etc/apache2/sites-available/000-default.conf

RUN apt-get clean
ADD docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod +x /docker-entrypoint.sh
ENTRYPOINT ["/docker-entrypoint.sh"]
