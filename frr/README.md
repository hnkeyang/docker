# frr-docker
frr 7.0 ubuntu docker base on [FRRouting/frr/docker/debian](https://github.com/FRRouting/frr/tree/master/docker/debian)

# Build
```
git clone https://github.com/hnkeyang/frr-docker.git  
cd frr-docker  
docker build .  

```

or use docker hub prebuild
```
docker pull hnkeyang/frr
```

# Run
```
docker run -t -d --name frr --privileged --restart=always frr
docker exec -it frr vtysh
```
