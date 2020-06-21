FROM markadams/chromium-xvfb-py3

RUN curl -o /usr/share/fonts/msyh.ttf https://raw.githubusercontent.com/chenqing/ng-mini/master/font/msyh.ttf && \
    mkfontdir && \
    mkfontscale && \
    fc-cache -f -v

COPY website_opentime.py /root

CMD /root/website_opentime.py
