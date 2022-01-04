import subprocess
import shutil
import urllib.request as request
from contextlib import closing
from datetime import datetime
import re
import ftplib


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

	out, error = ping.communicate()
	output_text = error.decode()
	matcher = re.compile("\d+:\d+\d+.\d+\d+")
	result = (matcher.search(output_text))
	result = result[0].translate((str.maketrans('', '', ':')))
	#print(result)
	return result

def ping_iperf(destination):
	string = "iperf -c " + destination
	ping=subprocess.Popen(string, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	out,error=ping.communicate()
	output_text=out.decode()
	array = output_text.split()
	result = array[-2]
	#print(result)
	return result

def ping_ftp(destination):

	# Fill Required Information
	HOSTNAME = destination
	USERNAME = "testuser"
	PASSWORD = "testuser"

	# Connect FTP Server
	ftp_server = ftplib.FTP(HOSTNAME, USERNAME, PASSWORD)

	# force UTF-8 encoding
	ftp_server.encoding = "utf-8"

	filename = "mlg2.img"

	# Write file in binary mode
	time1 = datetime.now()
	with open(filename, "wb") as file:
		# Command for Downloading the file "RETR filename"
		ftp_server.retrbinary(f"RETR {filename}", file.write)

	# Close the Connection
	ftp_server.quit()

	time2 = datetime.now()
	timing = time2 - time1
	timing2 = str(timing)
	matcher = re.compile("\d+\d+.\d+\d+\d+\d+")
	result = (matcher.search(timing2))
	# print(result[0])
	return result[0]
