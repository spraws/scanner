import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from dotenv import load_dotenv
import os
from pocketbase import PocketBase  
from pocketbase.client import FileUpload
import datetime



PB_USERNAME=os.getenv('PB_USER')
PB_PASSWORD=os.getenv('PB_PASS')

client = PocketBase('http://192.168.8.243:8090')

# authenticate as regular user
user_data = client.collection("users").auth_with_password(
    PB_USERNAME, PB_PASSWORD)
# check if user token is valid
user_data.is_valid

admin_data = client.admins.auth_with_password(PB_USERNAME, PB_PASSWORD)

# check if admin token is valid
admin_data.is_valid


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
        
        # data is stored in one string
        # parses data from string
        if "|" in text:
            parts = text.strip().split("|")
            for part in parts:
                if part.startswith("Name:"):
                    name = part.replace("Name:", "").strip()
                elif part.startswith("ID:"):
                    student_id = part.replace("ID:", "").strip()
                elif part.startswith("Date:"):
                    date = part.replace("Date:", "").strip()
        
        # print(f"Card ID: {id}")
        # print(f"Name: {name}")
        # print(f"Student ID: {student_id}")
        # print(f"Date: {date}")
        
        #returns variables for db
        return id, name, student_id, date, scanTime_str
    
    except Exception as e:
        print(f"Error: {e}")
        return None, None, None, None
    finally:
        GPIO.cleanup()

if __name__ == "__main__":
    card_id, name, student_id, date, scanTime_str = read_from_rfid()
        # Only stores if it reads data correctly
    if card_id and name and student_id and scanTime_str:
        data = {
            'Name': name,
            'student_id': student_id,
            'card_id': card_id,
            'scan_date': scanTime_str,
            
        }
        
    try:
        client.collection('attendance').create(data)
        print("Record Added")
    except Exception as error:
        print(f"Error adding record: {error}")
    print(data)
    
    
    
