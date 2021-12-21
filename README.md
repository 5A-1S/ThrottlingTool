# Routing architecture

3 tools will be used to implement a router in a linux docker machine

[http://pld.cs.luc.edu/courses/351/sum16/notes/iptables.html]

- iptables
- iproute2
- tc

## iptables

This tool will be used for basic firewall management.
This includes filter traffic, edit headers and if needed implement NAT for external connections.
It also works as a firewall, where we can filter traffic by IP or PORT.

## iproute2

This tool will be used to actually implement the routing.
It allows us to seperate incoming traffic and tretat it diferently according to a number of parameters, like source/destination IP, port, flags, payload, etc.

## tc
The tc tool is implemented in iproute2 and will alow us to actually throttle traffic using fair queuing or Tocken-Bucket approach.
Fair-queueing will handle traffic according to the existing available bandwidth, prioritizing some traffic over others.
Tocket-Bucket filter will have a fixed rate for traffic.


echo 1 > /proc/sys/net/ipv4/ip_forward


route add default gw 172.23.0.5
route del default gw 172.23.0.1

tc qdisc del dev eth0 root
tc qdisc add dev eth0 root handle 1: prio
tc qdisc add dev eth0 parent 1:1 handle 2: netem delay 500ms
tc filter add dev eth0 parent 1:0 protocol ip pref 55 handle ::55 u32 match ip dst 1.2.3.4 flowid 2:1

sudo tcpdump -i ethX icmp and icmp[icmptype]=icmp-echo

sudo tc qdisc add dev eth1 root handle 1: prio priomap 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
sudo tc qdisc add dev eth1 parent 1:2 handle 20: netem delay 3000ms
sudo tc filter add dev eth1 parent 1:0 protocol ip u32 match ip sport 7000 0xffff flowid 1:2

iperf -s
iperf -c 192.xxx
