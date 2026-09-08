from flask import Flask
from flask import render_template

app = Flask(__name__)

APP_ADDRESS = "0.0.0.0"
APP_PORT = 5000



@app.route("/", methods = ["GET", "POST"])
def hello_world():



app.config["DEBUG"] = True
app.run(host = APP_ADDRESS, port = APP_PORT)

