# Modules
from mfrc522 import MFRC522 as mfr
import RPi.GPIO as GPIO

#hi jonty :)

# Main Logic
reader = mfr()
status =  None
while status != reader.MI_OK:
	(status, TagType) = reader.Request(reader.PICC_REQIDL)
	if status == reader.MI_OK:
		print("Connection Success!")

import RPi.GPIO as GPIO
import MFRC522

#Create an instance of the MFRC522 reader 
MIFAREReader = MFRC522.MFRC522()

#Welcome Message
print("Looking for cards")

#Loop for card reading 
while True:
    #Scan for cards
    (status, TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)
    
    #If a card is found
    if status == MIFAREReader.MI_OK:
        print("Card Detected")
        
        #Get UID of the card
        (status, uid) = MIFAREReader.MFRC522_Anticoll()
        
        #if UID is recognised, continue
        if status == MIFAREReader.MI_OK:
            #Print UID
            print("Card read UID: %s, %s, %s, %s" % (uid[0], uid[1], uid[2], uid[3]))