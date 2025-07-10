import numpy as np
import csv

place_data = np.loadtxt("state_city.csv",delimiter=",",dtype=str)
place_lat = place_data[:, 0]
place_lon = place_data[:, 1]
place_city = place_data[:, 2]
place_state = place_data[:, 3]


data = [["user", "lat", "lon", "city", "state", "text"]]
f = open("data.csv", errors="ignore")

counter = 0
for line in f:
    # skip first line
    if counter == 0:
        counter +=1
        continue

    info = line.split(",")

    if(len(info) > 4):
        temp = info[3:]
        info = info[:4]
        text = ""
        for i in range(len(temp)):
            text += temp[i] + ","
        text = text[:-1]
        info[3] = text
    
    info[3] = info[3][:-1]

    lat, lon = info[1], info[2]


    indices = np.where(place_lat == lat)[0]

    city, state = "",""

    if indices.size == 0:
        print("OOPIES")
        continue


    if len(indices) > 1:
        for i in indices:
            if(place_lon[i] == lon):
                city = place_city[i]
                state = place_state[i]
                break
    else:
        city = place_city[indices[0]]
        state = place_state[indices[0]]

    user = info[0]
    text = info[3]


    data.append([user, lat, lon, city, state, text])

    
    counter += 1
    if counter % 50000 == 0:
        print(counter)

with open("final_data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(data)