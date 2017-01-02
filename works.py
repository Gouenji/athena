import getpass
from greet import get_greet
from weather import weather
from mail import mail
from tts import speak_a
from stt import active_listen
from time import time

passwd=getpass.getpass()

def start():
    startTime=time()
    speak_a(get_greet("hello"))
    speak_a("How can i Help u Sir, ")
    while True:
	    choice=active_listen()
	    if choice =='mail':
		mail(passwd)
	    elif choice =='weather':
	    	weather()
	    #elif choice=='command':
		#command()
	    elif choice == 'bye' or choice =='Bye' or choice == 'buy':
		speak_a(get_greet("goodbye"))
		return False
	    else:
		currentTime=time()
		if currentTime-startTime > 180:
			return True



