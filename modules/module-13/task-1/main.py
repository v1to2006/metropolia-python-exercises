from flask import Flask, jsonify

app = Flask(__name__)


def is_prime(number: int) -> bool:
    if number < 2:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False

    divisor = 3
    
    while divisor * divisor <= number:
        if number % divisor == 0:
            return False
        divisor += 2

    return True


@app.route("/prime-number/<int:number>", methods=["GET"])
def check_prime(number: int):
    return jsonify({
        "Number": number,
        "isPrime": is_prime(number)
    })


app.run(host="127.0.0.1", port=3000)