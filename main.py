#FIREBASE BRANCH

#This branch uses Google firetsore to store the data.
#This explains ho wthe code works https://www.youtube.com/watch?v=qsFYq_1BQdk - Jonty


import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import datetime


# Initialize Firebase Admin SDK
cred = credentials.Certificate(r"/home/dev/scanner/keys/attendance-159d3-firebase-adminsdk-fbsvc-084da24e95.json")
firebase_admin.initialize_app(cred)

# Get Firestore client
db = firestore.client()

# RFID Reader Setup
reader = SimpleMFRC522()

def read_from_rfid():
    try:
        print("Place your tag to read...")
        id, text = reader.read()
        
        name = None
        student_id = None
        date = None
        scanTime = datetime.datetime.now()
        scanTime_str = scanTime.strftime('%Y-%m-%d %H:%M:%S')
        
        # Data is stored in one string, parses the data from string
        if "|" in text:
            parts = text.strip().split("|")
            for part in parts:
                if part.startswith("Name:"):
                    name = part.replace("Name:", "").strip()
                elif part.startswith("ID:"):
                    student_id = part.replace("ID:", "").strip()
                elif part.startswith("Date:"):
                    date = part.replace("Date:", "").strip()
        
        # Print the values for debugging purposes
        print(f"Card ID: {id}")
        print(f"Name: {name}")
        print(f"Student ID: {student_id}")
        print(f"Date: {date}")
        print(f"Scan Time: {scanTime_str}")
        
        # Returns variables for DB
        return id, name, student_id, date, scanTime_str
    
    except Exception as e:
        print(f"Error: {e}")
        return None, None, None, None
    finally:
        GPIO.cleanup()

if __name__ == "__main__":
    # Get card details
    card_id, name, student_id, date, scanTime_str = read_from_rfid()

    # Only stores if it reads data correctly
    if card_id and name and student_id and date and scanTime_str:
        data = {
            'Name': name,
            'studentId': student_id,
            'uid': card_id,
            'scanTime': scanTime_str,
            'Date': date  # Add the date if required
        }
        
        # Save data to Firestore, use the name as the document ID
        doc_ref = db.collection('attendance').document(name).collection('logs').add(data)
        
        print(f'Attendance logged for {name} with Card ID: {card_id}')
    else:
        print("Error: Invalid RFID card data")
