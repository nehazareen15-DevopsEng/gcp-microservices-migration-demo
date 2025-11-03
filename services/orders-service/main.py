from flask import Flask, jsonify

app = Flask(__name__)

@app.get("/health")
def health():
    return jsonify(status="ok", service="orders-service")

@app.get("/orders")
def orders():
    return jsonify(orders=[{"id": 1, "item": "Book"}])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
