#In this final round of assessments, I've taken what I've done towards the realworld data of NASA monitored earthquakes, and applied it to another form of information they contain, wildfires. 

#Same process of importing the csv file from IDLE's main directory
import csv

#Uploading it and allowing the program to read it directly
with open("MODIS_C6_1_Global_24h.csv", "r", newline='', encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)

#Allowing the program to only display the brightness, location, confidence rating, and the coordinates of the wildfires, all within the top 10 from the csv itself.
    count = 0
    for row in reader:
        if count >= 10:
            break
        lat = float(row["latitude"])
        lon = float(row["longitude"])
        brightness = row["brightness"]
        confidence = row["confidence"]
        print(f"Fire detected at (lat: {lat:.3f}, lon: {lon:.3f}) | Brightness: {brightness} | Confidence: {confidence}")
        count += 1
