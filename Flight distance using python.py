# 🧭 Flight Distance & Time Estimator
# Author: Gavashkar Palanisamy
# Description: Calculates great-circle distance and flight time between two airports

import math

print("------ FLIGHT DISTANCE & TIME ESTIMATOR ------")

# Inputs
lat1 = float(input("Enter latitude of departure airport (in degrees): "))
lon1 = float(input("Enter longitude of departure airport (in degrees): "))
lat2 = float(input("Enter latitude of destination airport (in degrees): "))
lon2 = float(input("Enter longitude of destination airport (in degrees): "))
speed = float(input("Enter average cruise speed (in knots): "))

# Convert degrees to radians
lat1_r = math.radians(lat1)
lon1_r = math.radians(lon1)
lat2_r = math.radians(lat2)
lon2_r = math.radians(lon2)

# Earth radius in nautical miles
R = 3440.065

# Great circle distance formula
distance_nm = R * math.acos(
    math.sin(lat1_r) * math.sin(lat2_r)
    + math.cos(lat1_r) * math.cos(lat2_r) * math.cos(lon2_r - lon1_r)
)

# Estimated Time of Flight
time_hr = distance_nm / speed

print("\n------ FLIGHT DETAILS ------")
print(f"Distance (NM): {distance_nm:.2f}")
print(f"Estimated Time: {time_hr:.2f} hours")
print("-----------------------------------")
