#!/bin/bash

docker rm -f host_1
docker rm -f host_2
docker rm -f host_3
docker rm -f host_4
docker rm -f host_5
docker rm -f host_6
docker rm -f server_1
docker rm -f server_2

docker rm -f router

docker network rm cluster_1
docker network rm cluster_2