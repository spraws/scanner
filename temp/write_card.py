import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import time

reader = SimpleMFRC522()

def write_to_rfid(name, student_id):
    try:
        data = f"Name:{name}|ID:{student_id}|Date:{time.strftime('%Y-%m-%d %H:%M:%S')}"
        
        print("Place your tag to write...")
        reader.write(data)
        print("Written successfully!")
        
    except Exception as e:
        print(f"Error writing to card: {e}")
    finally:
        GPIO.cleanup()

def read_from_rfid():
    try:
        print("Place your tag to read...")
        id, text = reader.read()
    
        name = "Unknown"
        student_id = "Unknown"
        date = "Unknown"
        
        # Card can only store data in one string
        #parses string
        if "|" in text:
            parts = text.strip().split("|")
            for part in parts:
                if part.startswith("Name:"):
                    name = part.replace("Name:", "").strip()
                elif part.startswith("ID:"):
                    student_id = part.replace("ID:", "").strip()
                elif part.startswith("Date:"):
                    date = part.replace("Date:", "").strip()
        
        print("\nCard Contents:")
        print(f"Card ID: {id}")
        print(f"Name: {name}")
        print(f"Student ID: {student_id}")
        print(f"Date: {date}")
        print(f"Raw Text: {text}") 
        
        return id, name, student_id, date
        
    except Exception as e:
        print(f"Error reading card: {e}")
        return None, None, None, None
    finally:
        GPIO.cleanup()

if __name__ == "__main__":
    choice = input("Enter 'r' to read or 'w' to write: ")
    if choice.lower() == 'w':
        name = input("Enter Name: ")
        student_id = input("Enter Student ID: ")
        write_to_rfid(name, student_id)
    else:
        card_id, name, student_id, date = read_from_rfid()