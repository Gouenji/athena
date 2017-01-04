import getpass
from greet import get_greet
from weather import weather
from mail import mail
from tts import speak_a
from stt import active_listen
from calculator import calculator
from time import time

passwd=getpass.getpass()

def start():
    startTime=time()
    speak_a(get_greet("hello"))
    speak_a("How can i Help u  ")
    while True:
	    choice=active_listen().lower()
	    if 'mail' in choice:
		mail(passwd)
	    elif 'weather' in choice:
	    	weather()
	    elif 'calc' in choice:
		calculator()
	    elif choice == 'bye' or choice =='Bye' or choice == 'buy':
		speak_a(get_greet("goodbye"))
		return False
	    else:
		currentTime=time()
		if currentTime-startTime > 180:
			return True



