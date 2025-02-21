import mysql.connector
conn = mysql.connector.connect(
    host="",
    user="sprj1_23_dev",
    password="thisisatest",
    database="sprj1_23_attendance"
)
print("Connected successfully!")
conn.close()
