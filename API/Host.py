from Delay import *
import sys
import click
from pyfiglet import Figlet
from time import sleep

@click.command()
def exit_cli():
    print("Exiting")
    exit(1)


@click.command()
@click.option('--ip', prompt='Destination IP', type=click.STRING, help='Destination IP to test')
@click.option('--time', prompt='Time', type=click.INT, help='Duration of the test')
def ping_ip(ip, time):

    print("Testing ping on", ip)

    for i in range(time):
        sleep(1)
        result = ping_delay("172.22.0.3")

        print("Timeframe", i + 1, "s", "Delay = ", result, "ms")
        print("------------------------")


@click.command()
@click.option('--ip', prompt='Destination IP', type=click.STRING, help='Destination IP to test')
@click.option('--port', prompt='Destination Port', type=click.INT, help='Destion Port of the test')
@click.option('--time', prompt='Time', type=click.INT, help='Duration of the test')
def ping_port(ip, port, time):

    print("Testing ping on", ip, "port", port)

    for i in range(time):
        time.sleep(1)
        result = ping_port(ip, port)

        print("Timeframe", i + 1, "s", "Delay = ", result, "ms")
        print("------------------------")

@click.command()
@click.option('--ip', prompt='Destination IP', type=click.STRING, help='Destination IP to test')
def iperf_test(ip):

    print("Testing connection bandwidth on", ip)



action_map = {0: exit_cli, 1: ping_ip, 2: ping_port, 3:iperf_test}


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
    print("1 - Ping IP ICMP")
    print("2 - Ping IP Port")
    print("3 - Iperf Speedtest")
    print()


def startup():
    title = 'Throttling Detection Tool API'
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