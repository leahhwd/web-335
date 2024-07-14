"""
Title: harris_users1.py
Author: Leah Harris
Date: July 6, 2024
Description: Hands-On 4.2
"""

#Import MongoClient
from pymongo import MongoClient
import datetime

#Connection string to connect to client
client = MongoClient("mongodb+srv://web335_user:s3cret@bellevueuniversity.ijcdcml.mongodb.net/web335DBretryWrites=true&w=majority")
"""
I chose this connection string by selecting
Developer Tools/ MongoDB for VScode.
I'm not sure if this is the correct string
because it's slightly different than the example 
in the book. I manually added everything past ".net/"
that is included in the example. 
"""
#Configure variable to access web335 database
db = client['web335DB']

#Find all documents with projections 
for user in db.users.find({}, {"firstName": 1, "lastName": 1}):
    print(user)

#Find a document with employeeId 1011
print(db.users.find_one({"employeeId": "1011"}))

#Find a document with lastName Mozart
print(db.users.find_one({"lastName": "Mozart"}))
