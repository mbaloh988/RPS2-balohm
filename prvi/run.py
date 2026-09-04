from flask import Flask
app = Flask(__name__)

APP_ADDRESS = "0.0.0.0"
APP_PORT = 5000



@app.route("/", methods = ["GET", "POST"])
def hello_world():
    return "Hello 2.Ri! ♥"

app.config["DEBUG"] = True
app.run(host = APP_ADDRESS, port = APP_PORT)

