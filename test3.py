import pycurl
import certifi
from io import BytesIO
import warnings
import sys

warnings.filterwarnings("ignore",category=DeprecationWarning)
#name variable to use in testing
name="www.google.pt"


def website_speedtest(name):
	#website=sys.argv[0]
	c=pycurl.Curl()
	c.setopt(c.URL, name)

	#FOLLOWLOCATION Makes it go through redirections to avoid http 302 error
	#writefunction avoids printing the whole page

	c.setopt(pycurl.FOLLOWLOCATION,1)
	c.setopt(pycurl.WRITEFUNCTION,lambda bytes: len(bytes))
	c.perform()
	
	print ("HTTP response code",c.getinfo(c.HTTP_CODE))
	print ("effective URL",c.getinfo(c.EFFECTIVE_URL) )
	print ("time taken:",c.getinfo(c.TOTAL_TIME))
	print ("download speed:",c.getinfo(c.SPEED_DOWNLOAD)/1000000,"Megabytes per sec")
	print ("Redirect Time:",c.getinfo(c.REDIRECT_TIME),"Secs")
	print ("Connect Time:",c.getinfo(c.CONNECT_TIME),"Secs")
	print ("Name Look up Time:",c.getinfo(c.NAMELOOKUP_TIME),"Secs")
	speed=c.getinfo(c.SPEED_DOWNLOAD)/1000000

	c.close()
	return speed
	
website_speedtest(name)
