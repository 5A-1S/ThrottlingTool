import speedtest
import inspect
import ssl
import pycurl
from test3 import website_speedtest

def wait_input():
	key = "0"
	print("\n Alter your network settings or turn on your VPN")
	print("\n Press 1 to Continue when ready")
	while key not in ("1"):
		key=input()

def average_speed_test():
	totalspeed=0
	for x in range(0,5):
		print("\n Test number",x)
		totalspeed=totalspeed+(s.download()/1000000)
		final=totalspeed/6
		print("\n Average download speed is ",final)


ans=True
while ans:
	print("""
	Welcome to the Throttle Detection Tool
	Pick 1 to get default from speedtest
	Pick 2 to do 1 speedtest
	pick 3 to do an average conection speed test (5)
	Pick 4 to exit
	Pick 5 to do a speedtest on a website of your liking
	""")

	ssl._create_default_https_context = ssl._create_unverified_context
	s = speedtest.Speedtest()
	ans=input("What would u like to do?")
	
	
	if ans=="1":
		print("\n Testing for default")
		for method in inspect.getmembers(s,predicate=inspect.ismethod):
			print(method[0])
	elif ans=="2":
		s=speedtest.Speedtest()
		#print("Server list",s.get_servers())
		#s.set_mini_server('http://porto.speedtest.net.zon.pt:8080/speedtest/upload.php')
		print("\n Your current download speed is ",s.download()/1000000)
		print("\n Megabits!")
	elif ans=="3":
		average_speed_test()
	elif ans=="4":
		print("\n Exiting")
		ans=None
	elif ans=="5":
		#name="www.youtube.com"
		name=input("Enter website to test-> ")
		
		speed=website_speedtest(name)
		print("\n SPEED deste lado",speed,"Megabytes /s")
		
		wait_input()
		
		speed2=website_speedtest(name)
		print("\n Speed2",speed2,"Megabytes/s")
		
		speeddif=speed-speed2
		modspeed=abs(speeddif)
		percentage=((modspeed)/((speed+speed2)/2))*100
		print("percentage",percentage)
		if percentage<10 :
			print("No significant difference found")
		
		elif speed > speed2:
			print("\n Original conection speed is higher. Your conection isnt being throttled")
		elif speed2>speed:
			print("\n Conection speed improved in test #2. Your conection is probably being throttled")




		


		
