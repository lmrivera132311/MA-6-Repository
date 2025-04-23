#In this script below, I've demonstrated what I've learned about text replacement within the same string, and have applied it more real world examples, such as with NASA's realtime data for eathquakes. In this instance, the data comes form the first month or so
#series of earthquakes.

#First, I'll need to ask Python, or IDLE in that case, to upload any json files within its directory
import json

#From opening it, it should now begin to load it
with open("significant_month.geojson", "r") as f:
    data = json.load(f)

#Finally, I'll aallow Python to read the .csv file and grab the important parts, such as the coordinates, the location, and the points needed to show where the most amount of eathquakes appeared.
for feature in data["features"]:
    if feature["geometry"]["type"] == "Point":
        lon, lat = feature["geometry"]["coordinates"][:2]
        props = feature["properties"]
        mag = props.get("mag", "N/A")
        place = props.get("place", "Unknown location")
        print(f"Earthquake at (lat: {lat:.3f}, lon: {lon:.3f}) | Mag: {mag} | {place}")
