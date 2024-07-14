"""
Title: harris_usersp2.py
Author: Leah Harris
Date: July 13 2024
Description: Assignment 7.3
"""

#Import the MongoClient
from pymongo import MongoClient
import datetime

#Build connection string 
client = MongoClient("mongodb+srv://web335_user:s3cret@bellevueuniversity.ijcdcml.mongodb.net/web335DBretryWrites=true&w=majority")

#Variable to access web335DB
db = client['web335DB']

#Create new user document 
fieldman = {
    "firstName": "Sarah",
    "lastName": "Fieldman",
    "employeeId": "1014",
    "email": "sfieldman@me.com",
    "dateCreated": datetime.datetime.utcnow()
}

#Insert new document
fieldman_user_id = db.users.insert_one(fieldman).inserted_id
print(fieldman_user_id)

#Prove document creation
print(db.users.find_one({"employeeId": "1014"}))

#Update the email address of new document 
db.users.update_one(
    {"employeeId": "1014"},
    {
        "$set": {
            "email": "sarah.fieldman@me.com"
        }
    }
)

#Prove the document was updated
print(db.users.find_one({"employeeId": "1014"}))

#Delete the document that was created
result = db.users.delete_one({
    "employeeId": "1014"
})

#Prove the document was deleted
print(db.users.find_one({"employeeId": "1014"}))

