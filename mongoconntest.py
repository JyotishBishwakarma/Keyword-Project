from pymongo import MongoClient

def get_database():
 
   # Provide the mongodb atlas url to connect python to mongodb using pymongo
   #CONNECTION_STRING = "mongodb://localhost:27017/?serverSelectionTimeoutMS=5000&connectTimeoutMS=10000&3t.uriVersion=3&3t.connection.name=myconn&3t.alwaysShowAuthDB=true&3t.alwaysShowDBFromUserRole=true"
   CONNECTION_STRING = "mongodb+srv://user2:3zLzndId6IJZqUNO@cluster0.qaf3w2v.mongodb.net/mydb?retryWrites=true&w=majority"
 
   # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
   client = MongoClient(CONNECTION_STRING)
 
   # Create the database for our example (we will use the same database throughout the tutorial
   return client['mydb']
  
# This is added so that many files can reuse the function get_database()
if __name__ == "__main__":   
  
   # Get the database
   dbname = get_database()