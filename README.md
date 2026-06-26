Data Engineering Final Project – Environmental Sensor Pipeline

This project implements a batch data pipeline that loads environmental sensor data into a MongoDB database running inside a Docker container.

Dataset

Download the dataset manually from Kaggle before running the container:

https://www.kaggle.com/datasets/garystafford/environmental-sensor-data-132k

After the data is downloaded, olease place the file in the data/ folder.

Requirements


Have Docker installed on your machine


How to Run


Clone this repository.

Download the dataset and place it in the data/ folder (see above).

Build the Docker container.

Run the container.


The container will automatically:


Start MongoDB
Set up the database and collections
Load all sensor readings into MongoDB in batches


