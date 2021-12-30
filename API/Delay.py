import subprocess
import re
import sys


def ping_delay(destination):
	host=destination
	ping=subprocess.Popen(
	["ping","-c","1",host],
	stdout=subprocess.PIPE,
	stderr=subprocess.PIPE
	)
	out,error=ping.communicate()
	output_text=out.decode()
	matcher = re.compile("rtt min/avg/max/mdev = (\d+.\d+)")
	result=(matcher.search(output_text).groups(1))
	result=result[0].translate((str.maketrans('','','(')))
	#print(result)
	return result

def ping_delay_port(destination, port):

	string = "time nc -zw30 " + destination + " " + str(port)
	ping = subprocess.Popen(string, shell = True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

	out, error = ping.communicate(cd )
	output_text = error.decode()
	matcher = re.compile("\d+:\d+\d+.\d+\d+")
	result = (matcher.search(output_text))
	result = result[0].translate((str.maketrans('', '', ':')))
	#print(result)
	return result