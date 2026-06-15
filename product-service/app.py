from flask import Flask, jsonify
from prometheus_client import Counter, generate_latest
from prometheus_client import CONTENT_TYPE_LATEST

app = Flask(__name__)

REQUEST_COUNT = Counter(
    "product_service_requests_total",
    "Total requests to Product Service"
)

products = [
    {"id": 1, "name": "Laptop", "price": 80000},
    {"id": 2, "name": "Mobile", "price": 25000},
    {"id": 3, "name": "Keyboard", "price": 1500}
]

@app.route("/products")
def get_products():
    REQUEST_COUNT.inc()
    return jsonify(products)

@app.route("/products/<int:id>")
def get_product(id):
    REQUEST_COUNT.inc()

    for product in products:
        if product["id"] == id:
            return jsonify(product)

    return jsonify({"error": "Product not found"}), 404

@app.route("/metrics")
def metrics():
    return generate_latest(), 200, {
        "Content-Type": CONTENT_TYPE_LATEST
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
