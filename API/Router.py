import Docker
import subprocess
import sys
import click
from pyfiglet import Figlet
from time import sleep
from TC import TC


Client = Docker.Client()


@click.command()
def exit_cli():
    print("Exiting")
    exit(1)


@click.command()
def deploy_network():
    print("Initializing Docker Client")
    global Client

    print("Deploying Network")
    subprocess.run(["/Users/diogoremiao/Desktop/FEUP/TARSC/Lab2/Code/deploy_clusters.sh"])


@click.command()
def purge_network():
    print("Purging Network")
    subprocess.run(["/Users/diogoremiao/Desktop/FEUP/TARSC/Lab2/Code/purge_clusters.sh"])


@click.command()
def list_containers():
    global Client
    print("Listing All Containers")
    print(Client.list_all_containers_names())


@click.command()
@click.option('--interface', prompt='Interface', type=click.STRING, help='Interface for comms')
@click.option('--ip', prompt='Destination IP', type=click.STRING, help='Destination IP to delay')
@click.option('--delay', prompt='Delay', type=click.INT, help='Delay to apply')
def throttle_ip_dst(interface, ip, delay):
    global Client
    print("Applying delay to destination ip", ip)
    strings = TC.delay_ip_dst(interface, ip, delay)
    #print(*strings, sep="\n")
    for string in strings:
        Client.run_command("router", string)


@click.command()
@click.option('--interface', prompt='Interface', type=click.STRING, help='Interface for comms')
@click.option('--ip', prompt='Source IP', type=click.STRING, help='Srouce IP to delay')
@click.option('--delay', prompt='Delay', type=click.INT, help='Delay to apply')
def throttle_ip_src(interface, ip, delay):
    global Client
    print("Applying delay to source ip", ip)
    strings = TC.delay_ip_src(interface, ip, delay)
    #print(*strings, sep="\n")
    for string in strings:
        Client.run_command("router", string)


@click.command()
@click.option('--interface', prompt='Interface', type=click.STRING, help='Interface for comms')
@click.option('--port', prompt='Destination Port', type=click.STRING, help='Destination Port to delay')
@click.option('--delay', prompt='Delay', type=click.INT, help='Delay to apply')
def throttle_port_dst(interface, port, delay):
    global Client
    print("Applying delay to destination port", port)
    strings = TC.delay_port_dst(interface, port, delay)
    #print(*strings, sep="\n")
    for string in strings:
        Client.run_command("router", string)


@click.command()
@click.option('--interface', prompt='Interface', type=click.STRING, help='Interface for comms')
@click.option('--port', prompt='Source Port', type=click.STRING, help='Srouce Port to delay')
@click.option('--delay', prompt='Delay', type=click.INT, help='Delay to apply')
def throttle_port_src(interface, port, delay):
    global Client
    print("Applying delay to source port", port)
    strings = TC.delay_port_src(interface, port, delay)
    #print(*strings, sep="\n")
    for string in strings:
        Client.run_command("router", string)


@click.command()
@click.option('--interface', prompt='Interface', type=click.STRING, help='Interface for comms')
def clear_interface(interface):
    global Client
    print("Clearing Interface", interface)
    string = TC.clear_interface(interface)
    Client.run_command("router", string)

@click.command()
@click.option('--host', prompt='Host', type=click.STRING, help='Host to start server on')
def turn_on_iperf(host):
    global Client
    print("Starting Iperf endpoint on", host)

    Client.run_command(host, "iperf -s", detach=True)


@click.command()
@click.option('--host', prompt='Host', type=click.STRING, help='Host to start server on')
def turn_off_iperf(host):
    global Client
    print("Stopping Iperf endpoint on", host)

    Client.run_command(host, "pkill iperf", detach=True)

@click.command()
def turn_on_ftp():
    global Client
    print("Starting FTP endpoints on 172.22.0.5 and 172.23.0.5")

    Client.run_command("server_1", "systemctl start vsftpd", detach=True)
    Client.run_command("server_1", "systemctl enable vsftpd", detach=True)

    Client.run_command("server_2", "systemctl start vsftpd", detach=True)
    Client.run_command("server_2", "systemctl enable vsftpd", detach=True)


@click.command()
def turn_off_ftp():
    global Client
    print("Stopping FTP endpoints on 172.22.0.5 and 172.23.0.5")

    Client.run_command("server_1", "systemctl stop vsftpd", detach=True)
    Client.run_command("server_2", "systemctl stop vsftpd", detach=True)


action_map = {0: exit_cli, 1: deploy_network, 2: purge_network, 3: list_containers, 4: throttle_ip_dst, 5: throttle_ip_src, 6: throttle_port_dst, 7: throttle_port_src, 8: clear_interface, 9:turn_on_iperf, 10:turn_off_iperf, 11:turn_on_ftp, 12:turn_off_ftp}


@click.command()
@click.option('--action', prompt='Select a function', type=click.INT, help='Function to execute')
def test(action):
    if action in action_map.keys():
        action_map[action]()
    else:
        print("Invalid option!")


def help_options():
    print()
    print('--------Available actions--------')
    print("0  - Exit")
    print("1 - Deploy Network")
    print("2 - Purge Network")
    print("3 - List Containers")
    print("4 - Throttle Destination IP")
    print("5 - Throttle Source IP")
    print("6 - Throttle Destination Port")
    print("7 - Throttle Source Port")
    print("8 - Clear Interface")
    print("9 - Turn on Iperf Endpoint")
    print("10- Turn of Iperf Endpoint")
    print("11- Turn on FTP Endpoints")
    print("12- Turn off FTP Endpoints")
    print()


def startup():
    title = 'Throttling Tool API'
    f = Figlet()
    for x in f.renderText('TARSC'):
        print(x, end='')
        sys.stdout.flush()
        sleep(0.006)
    for x in title:
        print(x, end='')
        sys.stdout.flush()
        sleep(0.03)
    print('\n')


def main():
    startup()

    while True:
        try:
            help_options()
            test()
        except SystemExit as e:
            if e.code == 1:
                exit(1)
            continue


if __name__ == "__main__":
    main()
