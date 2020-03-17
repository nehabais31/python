"""
Neha Bais
Calculating area of Polygon enclosed by 4 cities 

"""

import math

def distance(lat1,lat2,lon1,lon2) :
    
    lat1 = math.radians(lat1)
    lat2 = math.radians(lat2)
    lon1 = math.radians(lon1)
    lon2 = math.radians(lon2)
    
    radius = 6371.01
    
    # Distance formula to calculate distance between 2 points
    
    d = radius * math.acos(
        math.sin(lat1) * math.sin(lat2) + 
        math.cos(lat1) * math.cos(lat2) * math.cos(lon1 - lon2))
    
    return (d)
    
    
# Co-ordinates for atlanta,charlotte,orlando & savannah in degrees
lat_atlanta   = 33.75
lon_atlanta   = 84.39
lat_charlotte = 35.23
lon_charlotte = 80.84
lat_orlando   = 28.54
lon_orlando   = 81.38
lat_savannah  = 32.08
lon_savannah  = 81.09

# Distance between Atlanta and Charlotte
a = distance(lat_atlanta, lat_charlotte, lon_atlanta, lon_charlotte)

# Distance between Atlanta and Orlando
b = distance(lat_atlanta, lat_orlando, lon_atlanta, lon_orlando)

# Distance between Orlando and Savannah
c = distance(lat_orlando, lat_savannah, lon_orlando, lon_savannah)

# Distance between Savannah and Charlotte
d = distance(lat_savannah, lat_charlotte, lon_savannah, lon_charlotte)

# Distance between Charlotte & Orlando
x = distance(lat_charlotte, lat_orlando, lon_charlotte, lon_orlando)

# Dividing the polygon into 2 triangles and calculating the areas
# Area enclosed between atlanta, charlotte & Orlando
s1 = (a + b + x)/2
area_aco = math.sqrt(s1 * (s1 - a) * (s1 - b) * (s1 - x))

# Area enclosed between Charlotte, Savannah & Orlando
s2 = (d + c + x)/2
area_cso = math.sqrt(s2 * (s2 - d) * (s2 - c) * (s2 - x))

# Area enclosed by polygon formed by all 4 cities
area = area_aco + area_cso

print ("Area enclosed by the 4 cities :" , round(area,2), "sq. km")

