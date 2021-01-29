# frr-docker
frr 7.0 ubuntu docker base on [FRRouting/frr/docker/debian](https://github.com/FRRouting/frr/tree/master/docker/debian)

# Build
```
git clone https://github.com/hnkeyang/docker-hnkeyang.git
cd docker-hnkeyang/frr
docker build .  

```

or use docker hub prebuild
```
docker pull hnkeyang/frr
```

# Run
```
docker run -itd --privileged --name frr hnkeyang/frr:latest
docker exec -it frr vtysh
```
