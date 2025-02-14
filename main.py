# Modules
from mfrc522 import MFRC522
import RPi.GPIO as GPIO

#hi jonty :)

# Main Logic
reader = MFRC522()

print("looking for cards")

while status != reader.MI_OK:
	(status, TagType) = reader.Request(reader.PICC_REQIDL)
	if status == reader.MI_OK:
		print("Connection Success!")

