from os import system

def speak_a(line):
	try:
		line=line.lower()
	except:
		pass

	line='google_speech -l en '+'\"'+line+'\"'
	system(line)
	system("clear")

def speak_a_h(line):
	try:
		line=line.lower()
	except:
		pass

	line='google_speech -l hi '+'\"'+line+'\"'
	system(line)
	system("clear")

def speak_d(line):
	try:
		line=line.lower()
	except:
		pass
	line='pico2wave -w cook.wav '+'\"'+line+'\"'+' && aplay cook.wav'
	system(line)
	system("rm cook.wav")

if __name__=="__main__":
	c=raw_input()
	speak_a(c)
