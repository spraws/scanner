import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import datetime


# Initialize Firebase Admin SDK
cred = credentials.Certificate(r"/home/dev/scanner/keys/attendance-159d3-firebase-adminsdk-fbsvc-084da24e95.json")
firebase_admin.initialize_app(cred)

# Get Firestore client
db = firestore.client()

person_ref = db.collection('attendance').document('Jonty Sprawson').collection('logs')

# Get all logs for "Bossman"
logs = person_ref.stream()

# Iterate over the logs and print them
for log in logs:
    print(log.id, log.to_dict())
    