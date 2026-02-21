from app.database import mongo

# Guardar un usuario de prueba
mongo.save_user(user_id=12345, username="Panda2078")
print("Usuario:", mongo.get_user(12345))

# Guardar un jugador de prueba
player_data = {
    "tag": "#ABC123",
    "name": "JugadorPrueba",
    "trophies": 2000,
    "clan": "ClanPrueba"
}
mongo.save_player(tag=player_data["tag"], data=player_data)
print("Jugador:", mongo.get_player(player_data["tag"]))

# Listar todos los jugadores
print("Todos los jugadores:", mongo.list_players())