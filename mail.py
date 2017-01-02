import imaplib
import email
import email.header
from datetime import datetime
from tts import speak_a
import getpass

def process_mailbox(M):
    rv, data = M.search(None, "ALL")
    if rv != 'OK':
        speak_a( "No messages found!")
        return

    for num in data[0].split():
        rv, data = M.fetch(num, '(RFC822)')
        if rv != 'OK':
            speak_a( "ERROR getting message"+str( num ))
            return

        msg = email.message_from_string(data[0][1])
        decode = email.header.decode_header(msg['Subject'])[0]
        subject = unicode(decode[0])
	speak_a('Message '+str(num))
	speak_a('From '+msg['From'].split('<')[0])
	speak_a(subject)
	print(subject)
        print 'Message %s: %s' % (num, subject)
        print 'Raw Date:', msg['Date']
	print msg
	c=raw_input()

        date_tuple = email.utils.parsedate_tz(msg['Date'])
        if date_tuple:
            local_date = datetime.fromtimestamp(email.utils.mktime_tz(date_tuple))
            print "Local Date:", \
                local_date.strftime("%a, %d %b %Y %H:%M:%S")
def mail(passwd):
	EMAIL_ACCOUNT = "compcode18@gmail.com"
	EMAIL_FOLDER = "INBOX"
	M = imaplib.IMAP4_SSL('imap.gmail.com')

	try:
	    rv, data = M.login(EMAIL_ACCOUNT,passwd )
	except imaplib.IMAP4.error:
	    speak_a( "LOGIN FAILED!!! ")
	    return
	print rv, data
	rv, mailboxes = M.list()
	#if rv == 'OK':
	    #print "Mailboxes:"
	    #print mailboxes

	rv, data = M.select(EMAIL_FOLDER)
	if rv == 'OK':
	    speak_a( "Processing mailbox...\n")
	    process_mailbox(M)
	    M.close()
	else:
	    speak_a( "ERROR: Unable to open mailbox "+str(rv))

	M.logout()
if __name__=="__main__":
	mail(getpass.getpass())

