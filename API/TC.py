import Docker

class TC:

    @staticmethod
    def clear_interface(interface):

        string = "tc qdisc del dev " + interface + " root"
        return string

    @staticmethod
    def delay_ip_dst(interface, ip, delay=500):

        string = []

        string.append("tc qdisc add dev " + interface + " root handle 1: prio")
        string.append("tc qdisc add dev " + interface + " parent 1:1 handle 2: netem delay " + str(delay) + "ms")
        string.append("tc filter add dev " + interface + " parent 1:0 protocol ip pref 55 handle ::55 u32 match ip dst " + str(ip) + " flowid 2:1")

        return string

    @staticmethod
    def delay_ip_src(interface, ip, delay=500):

        string = []

        string.append("tc qdisc add dev " + interface + " root handle 1: prio")
        string.append("tc qdisc add dev " + interface + " parent 1:1 handle 2: netem delay " + str(delay) + "ms")
        string.append("tc filter add dev " + interface + " parent 1:0 protocol ip pref 55 handle ::55 u32 match ip src " + str(ip) + " flowid 2:1")

        return string

    @staticmethod
    def delay_port_dst(interface, port, delay=500):

        string = []

        string.append("tc qdisc add dev " + interface + " root handle 1: prio priomap 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0")
        string.append("tc qdisc add dev " + interface + " parent 1:2 handle 20: netem delay " + str(delay) + "ms")
        string.append("tc filter add dev " + interface + " parent 1:0 protocol ip u32 match ip dport " + port + " 0xffff flowid 1:2")

        return string

    @staticmethod
    def delay_port_src(interface, port, delay=500):

        string = []

        string.append("tc qdisc add dev " + interface + " root handle 1: prio priomap 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0")
        string.append("tc qdisc add dev " + interface + " parent 1:2 handle 20: netem delay " + str(delay) + "ms")
        string.append("tc filter add dev " + interface + " parent 1:0 protocol ip u32 match ip sport " + port + " 0xffff flowid 1:2")

        return string


def main():

    print(TC.clear_interface("etho"))

    print("\n")

    string_list = TC.delay_ip_dst("eth0", "192.80.0.2")
    print(*string_list, sep="\n")
    string_list = TC.delay_ip_src("eth0", "192.80.0.2")
    print(*string_list, sep="\n")

    print("\n")

    string_list = TC.delay_port_dst("eth0", "5041")
    print(*string_list, sep="\n")
    string_list = TC.delay_port_src("eth0", "5041")
    print(*string_list, sep="\n")

if __name__ == "__main__":
    main()
