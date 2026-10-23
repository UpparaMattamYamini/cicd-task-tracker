
from flask import Flask, jsonify

app = Flask(__name__)


@app.get("/")
def home():
    return """
    <h1>My First CI/CD Project</h1>
    <p>Welcome to the Task Tracker application!</p>
    <p>My application is running successfully.</p>
    """


@app.get("/health")
def health():
    return jsonify({"status": "healthy"}), 200


@app.get("/tasks")
def get_tasks():
    return jsonify([]), 200


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
