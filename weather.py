import json
import urllib2 
import pprint
from stt import active_listen
from tts import speak_a,speak_a_h
def weather():
	try:    
		speak_a("Okay sir, Please tell me the city ")	
		city =active_listen()
	except:
		city="kharagpur"
	city+=',in'	
	pp = pprint.PrettyPrinter(indent=4)
	API_KEY = "9294d3ed0680074c429b6f1e653d8800"
	CITY_NAME = city
	try:
	    f = urllib2.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' \
		            + CITY_NAME + '&units=metric' + '&APPID=' +  API_KEY)
	    respond_raw = f.read()
	except:
		print 'Execption: URL is not correct!'
		raise
	weather_dict = json.loads(respond_raw)
	pp.pprint(weather_dict)
	#", Lat "+str(weather_dict['coord']['lat']) + " Lon "+str(weather_dict['coord']['lon'])+
	line=('\n\n' +" \n, , "+ weather_dict['weather'][0]['description'] +',minimum temperature: ' + str(weather_dict['main']['temp_min'])+',maximum temperature: ' + str(weather_dict['main']['temp_max'])+', humidity: ' + str(weather_dict['main']['humidity']) + '%.' )
	try:	
		speak_a('here is the weather for ')
		speak_a_h(weather_dict['name'])
		speak_a(line)
	except:	
		print (line)

if __name__=="__main__":
	weather()

