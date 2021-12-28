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
