#!/bin/bash
docker pull diogoremiao/ubuntu_host:latest
docker pull diogoremiao/ubuntu_router:latest
docker pull diogoremiao/ubuntu_server:latest

docker network create --subnet=172.22.0.0/16 cluster_1
docker network create --subnet=172.23.0.0/16 cluster_2

docker run --privileged -d -it --net=cluster_1 --name=host_1 diogoremiao/ubuntu_host
docker run --privileged -d -it --net=cluster_1 --name=host_2 diogoremiao/ubuntu_host
docker run --privileged -d -it --net=cluster_1 --name=host_3 diogoremiao/ubuntu_host
docker run --privileged -d -it --net=cluster_1 --name=server_1 diogoremiao/ubuntu_server

docker run --privileged -d -it --net=cluster_2 --name=host_4 diogoremiao/ubuntu_host
docker run --privileged -d -it --net=cluster_2 --name=host_5 diogoremiao/ubuntu_host
docker run --privileged -d -it --net=cluster_2 --name=host_6 diogoremiao/ubuntu_host
docker run --privileged -d -it --net=cluster_2 --name=server_2 diogoremiao/ubuntu_server

docker run --privileged -d -it --net=cluster_1 --name=router diogoremiao/ubuntu_router

docker network connect cluster_2 router


docker exec -it host_1 route add default gw 172.22.0.6
docker exec -it host_2 route add default gw 172.22.0.6
docker exec -it host_3 route add default gw 172.22.0.6
docker exec -it server_1 route add default gw 172.22.0.6

docker exec -it host_1 route del default gw 172.22.0.1
docker exec -it host_2 route del default gw 172.22.0.1
docker exec -it host_3 route del default gw 172.22.0.1
docker exec -it server_1 route del default gw 172.22.0.1

docker exec -it host_4 route add default gw 172.23.0.6
docker exec -it host_5 route add default gw 172.23.0.6
docker exec -it host_6 route add default gw 172.23.0.6
docker exec -it server_2 route add default gw 172.23.0.6

docker exec -it host_4 route del default gw 172.23.0.1
docker exec -it host_5 route del default gw 172.23.0.1
docker exec -it host_6 route del default gw 172.23.0.1
docker exec -it server_2 route del default gw 172.23.0.1