import mysql.connector
from geopy.distance import geodesic

DB_CONFIG = {
	"host": "127.0.0.1",
	"port": 3306,
	"user": "admin",
	"password": "admin",
	"database": "flight_game"
}

def get_airport_coordinates(connection, icao):
	cursor = connection.cursor()
	query = f"SELECT latitude_deg, longitude_deg FROM {DB_CONFIG["database"]}.airport WHERE ident=\"{icao}\""

	cursor.execute(query)

	row = cursor.fetchone()
	cursor.close()
	return row

def calculate_airports_distance(airport1, airport2):
	return geodesic(airport1, airport2).km

def main():
	connection = mysql.connector.connect(**DB_CONFIG)

	airport1 = get_airport_coordinates(connection, input("Enter first airport ICAO-code: "))
	airport2 = get_airport_coordinates(connection, input("Enter second airport ICAO-code: "))

	distance = calculate_airports_distance(airport1, airport2)

	print(f"Distance: {distance:.2f} km")

main()