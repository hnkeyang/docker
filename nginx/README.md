
# ENV nginx worker processess default 4,
NGINX_WORK_PROCESS


# 2 worker
docker run --rm --name ngx -e NGINX_WORK_PROCESS=2 hnkeyang/nginx


