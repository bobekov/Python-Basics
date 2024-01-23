from math import floor

records_seconds = float(input())
distance_meters = float(input())
time_seconds_meters = float(input())

resistance = floor(distance_meters / 15) * 12.5
distance = distance_meters * time_seconds_meters + resistance

if distance >= records_seconds:
    print(f"No, he failed! He was {distance - records_seconds:.2f} seconds slower.")
else:
    print(f"Yes, he succeeded! The new world record is {distance:.2f} seconds.")