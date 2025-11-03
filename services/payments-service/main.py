from flask import Flask, jsonify

app = Flask(__name__)

@app.get("/health")
def health():
    return jsonify(status="ok", service="payments-service")

@app.get("/payments")
def payments():
    return jsonify(payments=[{"id": 100, "amount": 25.5}])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=6000)
