from flask import Flask, jsonify

app = Flask(__name__)

products = [
    {
        "id": 1,
        "name": "Laptop",
        "price": 80000
    },
    {
        "id": 2,
        "name": "Mobile",
        "price": 25000
    },
    {
        "id": 3,
        "name": "Keyboard",
        "price": 1500
    }
]

@app.route("/products")
def get_products():
    return jsonify(products)

@app.route("/products/<int:id>")
def get_product(id):
    for product in products:
        if product["id"] == id:
            return jsonify(product)

    return jsonify({"error": "Product not found"}), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)