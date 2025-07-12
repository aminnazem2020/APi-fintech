from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/price")
def get_price():
    return jsonify({"symbol": "AAPL", "price": 198.23})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
