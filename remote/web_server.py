from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route("/")
def root():
    return send_from_directory('public', "index.html")
