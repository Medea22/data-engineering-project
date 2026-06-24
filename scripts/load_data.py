import csv
from pymongo import MongoClient

def load_data():
    # Connect to MongoDB
    client = MongoClient("mongodb://localhost:27017/")
    db = client["city_sensors"]
    collection = db["sensor_readings"]

    batch = []
    batch_size = 1000
    total = 0

    print("Reading CSV file...")

    with open("data/iot_telemetry_data.csv", "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Convert numeric fields from string to float
            row["temp"] = float(row["temp"])
            row["humidity"] = float(row["humidity"])
            row["co"] = float(row["co"])
            row["lpg"] = float(row["lpg"])
            row["smoke"] = float(row["smoke"])
            row["light"] = row["light"] == "True"
            row["motion"] = row["motion"] == "True"

            batch.append(row)

            # Insert in batches of 1000
            if len(batch) == batch_size:
                collection.insert_many(batch)
                total += len(batch)
                batch = []
                print(f"  Inserted {total} records...")

    # Insert any remaining records
    if batch:
        collection.insert_many(batch)
        total += len(batch)

    print(f"Total records inserted: {total}")
    client.close()

if __name__ == "__main__":
    load_data()