import json
import pymongo

file1 = open("Game.json","r")
file2 = open("Players.json","r")

games_str = file1.read()
players_str = file2.read()

data1 = json.loads(games_str)
data2 = json.loads(players_str)

print(data1[0]["G_Name"])
print(data2[1]["Name"])

for rows in range(len(data1)):  
    for col in data1[rows]:
        print(data1[rows][col], end = " ")


    