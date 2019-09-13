# import imaplib
import imapclient
conn=imapclient.IMAPClient('imap.gmail.com',ssl=True)
conn.login('login@gmail.com','Password')
conn.select_folder('INBOX',readonly=True)
UIDs=conn.search(['SINCE 20-Aug-2015'])
UIDs_Number=UIDs[1]
conn.fetch([UIDs_Number],['BODY[]','FLAGS'])

rawMessage=conn.fetch([UIDs_Number],['BODY[]','FLAGS'])
import pyzmail
message=pyzmail.PyzMessage.factory(rawMessage[UIDs_Number],['BODY[]','FLAGS'])
message.get_address('from')
message.get_address('bcc')
message.text_part()
conn.list_folders()
