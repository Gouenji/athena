from stt import active_listen
from tts import speak_a

def calculate(line):

	try:	
		line=line.replace("plus",'+').replace("minus",'-').replace("into",'*').replace("by",'/')
		line.replace('seven','7').replace('nine','9').replace('ten','10')
	except:
		pass
		
	print line
	ans=eval(line)

	speak_a(str(ans))


def calculator():
        print "starting.....\nspeak the arithmetic expression \nsay end to complete and compute \n and back to delete the last said literal"
	print"Listening"

	Expression=''
	while(1):
		line=active_listen()
		if ('end' in line or 'and' in line):
			print "breaking"
			break
		if ('back' in line or 'bat' in line or 'bag' in line or 'mach' in line or 'mac' in line):
			Expression=Expression[:Expression.rfind(' ')]
			print "deleting"
			print (Expression)
			continue
		Expression+=line+' '
		print (Expression)

	Expression.strip(' ')	
	print Expression	
	calculate(Expression)

	print "ending..."
	
if __name__=="__main__":
			
	calculator()
