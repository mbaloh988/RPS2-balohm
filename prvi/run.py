from flask import Flask
app = Flask(__name__)

APP_ADDRESS = "0.0.0.0"
APP_PORT = 5000

app.config["DEBUG"] = True
app.run(host = APP_ADDRESS, port = APP_PORT)

@app.route("/")
def hello_world():
    return "Hello 2.Ri! ♥"