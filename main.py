# Modules
import RPi.GPIO as GPIO
import mfrc522

#hi jonty :)

# Main Logic

status =  None
#Create an instance of the MFRC522 reader 
MIFAREReader = mfrc522.MFRC522()

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