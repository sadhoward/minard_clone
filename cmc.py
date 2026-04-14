with open("data/minard.txt") as f:
    lines = f.readlines()

column_names = lines[2].split()
print(column_names)

patterns_to_be_replaced = {"(", ")", "$", ","}
adjusted_column_names = []
for column_name in column_names:
    for pattern in patterns_to_be_replaced:
        if pattern in column_name:
            column_name = column_name.replace(pattern, "")
    adjusted_column_names.append(column_name)
print(adjusted_column_names)

column_names_city = adjusted_column_names[:3]
column_names_temperature = adjusted_column_names[3:7]
column_names_troop = adjusted_column_names[7:]
print(column_names_city)
print(column_names_temperature)
print(column_names_troop)

i = 6
longitudes, latitudes, cities = [], [], []
while i <= 25:
    long, lat, city = lines[i].split()[:3]
    longitudes.append(float(long))
    latitudes.append(float(lat))
    cities.append(city)
    i += 1
city_data = (longitudes, latitudes, cities)
for data in city_data:
    print(data)

import pandas as pd

city_df = pd.DataFrame()
for column_name, data in zip(column_names_city, city_data):
    city_df[column_name] = data
city_df