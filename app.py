from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)

# Enable CORS
CORS(app)


if __name__ == '__main__':
    app.run()