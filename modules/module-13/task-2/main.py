from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)


def get_connection():
    return mysql.connector.connect(
        host="127.0.0.1",
        port=3306,
        database="flight_game",
        user="root",
        password="salasana",
        autocommit=True
    )


@app.route("/airport/<icao>", methods=["GET"])
def get_airport(icao: str):
    connection = get_connection()
    cursor = connection.cursor()

    sql = """
        SELECT ident, name, municipality
        FROM airport
        WHERE ident = %s
    """
    cursor.execute(sql, (icao.upper(),))
    result = cursor.fetchone()

    cursor.close()
    connection.close()

    if result is None:
        return jsonify({"error": "Airport not found"}), 404

    return jsonify({
        "ICAO": result[0],
        "Name": result[1],
        "Municipality": result[2]
    })


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=3000)