import mysql.connector
from dotenv import load_dotenv
import os

db_host=os.getenv("SQL_SERVER")
db_user=os.getenv("SQL_USER")
db_passwd=os.getenv("SQL_PASSWORD")
db_db=os.getenv("SQL_DATABASE")

# connect = mysql.connector.connect(
#     host=db_host,
#     user=db_user,
#     password=db_passwd,
#     database=db_db
# )

# #establish conn
# cursor = connect.cursor()
# print("Connected successfully!")
# connect.close()

print(db_passwd)
