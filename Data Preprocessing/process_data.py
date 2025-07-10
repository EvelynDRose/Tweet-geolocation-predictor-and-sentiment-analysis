import csv


# Turn full_text.txt into .csv
f = open("full_text.txt", errors="ignore")

data = [["user", "lat", "lon", "text"]]

counter = 0
for line in f:
    user, time, cords, lat, lon, text = line.split("\t")
    text = text[:-1]
    
    data.append([user, lat, lon, text])
    counter += 1

    if counter % 50000 == 0:
        print(counter)

with open("data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(data)



# Turn state_city.txt into .csv
f = open("state_city.txt", errors="ignore")

data = [["lat", "lon", "city", "state"]]

counter = 0
bad = 0
for line in f:
    place = line.split("\t")
    
    # cleaning line
    if(place[-1] == "\n"):
        place = place[:-1]

    # removeing non city,state combos
    if(len(place) < 3 or place[-1] == ""):
        bad += 1
        continue

    # cleaning state
    place[-1] = place[-1][:-1]

    lat, lon, city, state = [],[],[],""

    if len(place) == 3:
        lat, lon, city = place[0], place[1], place[2]
    else:
        lat, lon, city, state = place[0], place[1], place[2], place[3]
    
    data.append([lat, lon, city, state])
    counter += 1

    if counter % 10000 == 0:
        print(counter)
print("Bad: ", bad)

with open("state_city.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(data)