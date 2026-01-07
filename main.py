# main.py
from flask import Flask, jsonify
from model import obter_status

app = Flask(__name__)

@app.route("/status")
def status():
    return jsonify(obter_status())

if __name__ == "__main__":
    app.run(debug=True)
