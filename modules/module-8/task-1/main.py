import mysql.connector

DB_CONFIG = {
	"host": "127.0.0.1",
	"port": 3306,
	"user": "admin",
	"password": "admin",
	"database": "flight_game"
}

def get_airport(connection, icao):
	query = f"SELECT name, iso_country FROM flight_game.airport WHERE ident=\"{icao}\""
	cursor = connection.cursor()

	cursor.execute(query)

	row = cursor.fetchone()
	cursor.close()

	return row

def print_row(row):
	if row == None:
		print("Not found")
		return
	
	for i in row:
		print(i)

def main():
	connection = mysql.connector.connect(**DB_CONFIG)

	icao = input("Enter ICAO-code: ")
	row = get_airport(connection, icao)
	print_row(row)

main()