from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/ping", methods=["GET"])
def ping():
    return jsonify({
        "message": "MLOps API is running!"
    })


@app.route("/greet", methods=["GET"])
def greet():
    name = request.args.get("name", "Guest")

    return jsonify({
        "message": f"Hello, {name}!"
    })


@app.route("/sum", methods=["POST"])
def calculate_sum():
    data = request.get_json()

    if not data or "a" not in data or "b" not in data:
        return jsonify({
            "error": "Please provide a and b"
        }), 400

    return jsonify({
        "sum": data["a"] + data["b"]
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050)