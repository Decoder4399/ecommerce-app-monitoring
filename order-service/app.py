from flask import Flask, jsonify
import requests

app = Flask(__name__)

orders = [
    {
        "order_id": 1001,
        "product_id": 1,
        "quantity": 2
    },
    {
        "order_id": 1002,
        "product_id": 2,
        "quantity": 1
    }
]

@app.route("/orders")
def get_orders():
    return jsonify(orders)

@app.route("/order/<int:id>")
def get_order(id):

    for order in orders:

        if order["order_id"] == id:

            product = requests.get(
                f"http://product-service:5001/products/{order['product_id']}"
            ).json()

            return jsonify({
                "order": order,
                "product": product
            })

    return jsonify({"error":"Order not found"}),404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)