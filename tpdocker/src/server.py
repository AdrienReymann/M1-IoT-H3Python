from flask import Flask
import os

server = Flask(__name__)

@server.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    server.run(host='0.0.0.0', port=port)