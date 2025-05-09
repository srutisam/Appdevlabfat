from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify(message="Welcome to the Python Web Application!")

@app.route("/greet/<username>")
def greet(username):
    return jsonify(message=f"Hello, {username}!")

if __name__ == "__main__":
    app.run(debug=True)
