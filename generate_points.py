from shapely.geometry import Point, MultiPolygon
from shapely.wkt import loads
import random

# Define the MULTIPOLYGON
polygon_string = "SRID=4326;MULTIPOLYGON (((12.969445 77.58271, 12.935262 77.582052, 12.935064 77.633246, 12.971075 77.627784, 12.969445 77.58271), (12.994512 77.527236, 12.994669 77.482603, 12.951332 77.480998, 12.952897 77.547465, 12.994512 77.527236), (13.022044 77.634161, 13.024077 77.709298, 12.979181 77.711867, 12.973236 77.642992, 13.022044 77.634161)))"

# Create a Shapely MultiPolygon object using loads from WKT
multipolygon = loads(polygon_string.split(';')[-1])  # Extract the WKT part and create the MultiPolygon

# Function to generate a random point within the bounding box of the polygon
def generate_random_point_within_polygon(multipolygon):
    min_x, min_y, max_x, max_y = multipolygon.bounds
    while True:
        # Generate random coordinates within the bounding box
        random_point = Point(random.uniform(min_x, max_x), random.uniform(min_y, max_y))
        # Check if the generated point falls within the polygon
        if multipolygon.contains(random_point):
            return random_point

# Generate a random point within the given MULTIPOLYGON
random_point_within_polygon = generate_random_point_within_polygon(multipolygon)
print("Random point within the MULTIPOLYGON:", random_point_within_polygon)

