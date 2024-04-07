import pymongo

from pymongo import MongoClient 
client = MongoClient('mongodb://localhost:27017') 
db = client['pycharm']  # Replace 'your_database_name' with your actual database 

collection = db['user']  # Replace 'your_collection_name' with your actual 

# Insert multiple documents 
data_to_insert = [{'name': 'mohit', 'course': 'MBA', 'Roll': '1', 'age': '20'}, 
{'name': 'aniket', 'course': 'BBA', 'Roll': '2', 'age': '22'}, 
{'name': 'ramesh', 'course': 'MCA', 'Roll': '3', 'age': '24'}] 
result = collection.insert_many(data_to_insert)