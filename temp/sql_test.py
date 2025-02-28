from pocketbase import PocketBase  
from pocketbase.client import FileUpload
import os

PB_USERNAME=os.getenv('PB_USER')
PB_PASSWORD=os.getenv('PB_PASS')

client = PocketBase('http://192.168.7.87:8090')

# authenticate as regular user
user_data = client.collection("users").auth_with_password(
    PB_USERNAME, PB_PASSWORD)
# check if user token is valid
user_data.is_valid

# or as admin
admin_data = client.admins.auth_with_password(PB_USERNAME, PB_PASSWORD)

# check if admin token is valid
admin_data.is_valid

# list and filter "example" collection records
result = client.collection("users").get_list()
print(result)

# # create record and upload file to image field
# result = client.collection("example").create(
#     {
#         "status": "true",
#         "image": FileUpload(("image.png", open("image.png", "rb"))),
#     })

# # and much more...