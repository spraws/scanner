import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

def read_from_rfid():
    try:
        print("Place your tag to read...")
        id, text = reader.read()
        
        name = None
        student_id = None
        date = None
        
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
        return id, name, student_id, date
    
    except Exception as e:
        print(f"Error: {e}")
        return None, None, None, None
    finally:
        GPIO.cleanup()

if __name__ == "__main__":
    card_id, name, student_id, date = read_from_rfid()
    print(card_id, name, student_id, date)