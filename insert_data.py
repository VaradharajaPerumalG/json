import json
from pymongo.mongo_client import MongoClient

db_uri = "mongodb+srv://VaradharajaPerumal:54410@varadharajaperumal.jlcs4d1.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(db_uri)

db_name = "gaming_industry"
col_games = "game"
col_players = "players"

db = client[db_name]
games = db[col_games]
players = db[col_players]

file1 = open("Game.json","r")
file2 = open("Players.json","r")

games_str = file1.read()
players_str = file2.read()

data1 = json.loads(games_str)
data2 = json.loads(players_str)

for i in data1:
    games.insert_one(i)
    for j in data2:
        players.insert_one(j)