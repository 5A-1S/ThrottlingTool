from Delay import *
import click
from pyfiglet import Figlet
from time import sleep
import sys
import subprocess

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
        result = ping_delay(ip)

        print("Timeframe", i + 1, "s", "Delay = ", result, "ms")
        print("------------------------")


@click.command()
@click.option('--ip', prompt='Destination IP', type=click.STRING, help='Destination IP to test')
@click.option('--port', prompt='Destination Port', type=click.INT, help='Destion Port of the test')
@click.option('--time', prompt='Time', type=click.INT, help='Duration of the test')
def ping_port(ip, port, time):

    print("Testing ping on", ip, "port", port)

    for i in range(time):
        sleep(1)
        result = ping_delay_port(ip, port)

        print("Timeframe", i + 1, "s", "Delay = ", result, "ms")
        print("------------------------")

@click.command()
@click.option('--ip', prompt='Destination IP', type=click.STRING, help='Destination IP to test')
def iperf_test(ip):

    print("Testing connection bandwidth on", ip)

    result = ping_iperf(ip)

    print("Connection Bandwidth:", result, "Gbits/s")


@click.command()
@click.option('--ip', prompt='Destination IP', type=click.STRING, help='Destination IP to test')
@click.option('--times', prompt='Number of Times', type=click.INT, help='Number of times to download')
def ftp_test(ip, times):

    print("Testing connection bandwidth on", ip)

    for i in range(times):

        result = ping_ftp(ip)

        bandwidth = 1073741824 / float(result) / 1024 / 1024

        subprocess.run(["rm mlg2.img"])

        print("Connection Bandwidth Test ", i+1, ":", round(bandwidth), "Mbits/s")





action_map = {0: exit_cli, 1: ping_ip, 2: ping_port, 3:iperf_test, 4:ftp_test}


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
    print("4 - FTP Speedtest")
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
