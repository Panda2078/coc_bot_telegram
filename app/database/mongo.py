from pymongo import MongoClient
from app.config import settings

client = MongoClient(settings.MONGO_URI)
db = client.get_default_database()

users_col = db["users"]
players_col = db["players"]

def save_user(user_id: int, username: str):
    users_col.update_one({"user_id": user_id}, {"$set": {"username": username}}, upsert=True)

def get_user(user_id: int):
    return users_col.find_one({"user_id": user_id})

def save_player(tag: str, data: dict):
    players_col.update_one({"tag": tag}, {"$set": data}, upsert=True)

def get_player(tag: str):
    return players_col.find_one({"tag": tag})

def list_players():
    return list(players_col.find({}))