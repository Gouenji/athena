import speech_recognition as sr
import os
def active_listen():

    r = sr.Recognizer()
    with sr.Microphone() as src:
    	audio = r.listen(src)
    #print msg
    msg = ''
    try:
        msg = r.recognize_google(audio) 
	print (msg.lower())
    #except sr.UnknownValueError:
    #    print("Google Speech Recognition could not understand audio")
    #except sr.RequestError as e:
    #    print("Could not request results from Google STT; {0}".format(e))
    #except:
    #    print("Unknown exception occurred!")
    finally:
        return msg.lower()

def active_listen_2():
    r = sr.Recognizer()
    with sr.Microphone() as src:
    	audio = r.listen(src)
    print audio
    msg = ''
    try:
        msg = r.recognize_google(audio) 
	print (msg.lower())
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google STT; {0}".format(e))
    except:
        print("Unknown exception occurred!")
    finally:
        return msg.lower()

if __name__=="__main__":
	active_listen_2()
