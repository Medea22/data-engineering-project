from pymongo import MongoClient

def setup_database():
    client = MongoClient("mongodb://localhost:27017/")
    
    db = client["city_sensors"]
    collection = db["sensor_readings"]
    
    collection.create_index("ts")
    collection.create_index("device")
    
    print("Database and collection set up successfully!")
    client.close()

if __name__ == "__main__":
    setup_database()