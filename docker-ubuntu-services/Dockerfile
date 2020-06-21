FROM hnkeyang/ubuntu-systemd-ssh:18.04

RUN apt-get update && \
    apt-get install -y \
    vsftpd \
    telnetd xinetd \
    && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN systemctl enable vsftpd
RUN systemctl enable xinetd

RUN useradd -m test && echo test:test|chpasswd
