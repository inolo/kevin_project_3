"""
Here is your response. JSON data format is used in a wide variety of applications. It is almost a universal way to send
data between applications.

Here is an example response from an api where you send in an image of a car, and it reads the images and gives you the plate,
make and model, color, type of vehicle, and a bounding box coordinate of the image.

I want you to parse this data out and then use it to insert into an sqlite database that you have to create.

The sqlite database will be named "sqlite.db" and create a table called vehicle_results.
The columns you will need to insert into the table will be:

(timestamp, plate, score (plate_core), vehicle_make, vehicle_model, vehicle_type, color)


Your job is to parse this json and insert the correct data into the database.
"""

response = {
    "processing_time": 288.758,
    "results": [
        {
            "box": {
                "xmin": 143,
                "ymin": 481,
                "xmax": 282,
                "ymax": 575
            },
            "plate": "nhk552",
            "region": {
                "code": "gb",
                "score": 0.747
            },
            "vehicle": {
                "score": 0.798,
                "type": "Sedan",
                "box": {
                    "xmin": 67,
                    "ymin": 113,
                    "xmax": 908,
                    "ymax": 653
                }
            },
            "score": 0.904,
            "candidates": [
                {
                    "score": 0.904,
                    "plate": "nhk552"
                }
            ],
            "dscore": 0.99,
            "model_make": [
                {
                    "make": "Riley",
                    "model": "RMF",
                    "score": 0.306
                }
            ],
            "color": [
                {
                    "color": "black",
                    "score": 0.937
                }
            ],
            "orientation": [
                {
                    "orientation": "Front",
                    "score": 0.937
                }
            ]
        }
    ],
    "filename": "1617_7M83K_car.jpg",
    "version": 1,
    "camera_id": None,
    "timestamp": "2020-10-12T16:17:27.574008Z"
}

import sqlite3

conn = sqlite3.connect("./sqlite.db")

conn.execute("""
            CREATE TABLE VEHICLE_RESULTS
            (timestamp date,
            plate varchar2(50),
            score number,
            vehicle_make varchar2(25),
            vehicle_model varchar2(25),
            vehicle_type varchar2(25),
            color varhcar2(25)); """)


time = response["timestamp"]
print(time)
plate = response['results'][0]['plate']
print(plate)
score = response['results'][0]['region']['score']
print(score)
make = response['results'][0]['model_make'][0]['make']
print(make)
model = response['results'][0]['model_make'][0]['model']
print(model)
vehicle_type = response['results'][0]['vehicle']['type']
print(vehicle_type)
color = response['results'][0]['color'][0]['color']
print(color)

conn.execute(""" INSERT INTO VEHICLE_RESULTS 
                  (timestamp,
                  plate, 
                  score,
                  vehicle_make,
                  vehicle_model,
                  vehicle_type,
                  color)
                  values (?,?,?,?,?,?,?)""", (time, plate, score, make, model, vehicle_type, color))
conn.commit()
