from flask import Flask, jsonify, make_response

app = Flask(__name__)


@app.get("/")
def home_controller():
    return make_response(jsonify({"message": "Welcome to flask app", "status": 200}))


if __name__ == "__main__":
    app.run("0.0.0.0", port=8888, debug=False)
