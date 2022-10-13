from flask import Flask, jsonify, render_template, request
import time

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/list", methods=["GET"])
def list():
    # create sample list to be added to options dropwdown
    time.sleep(2)  # 1 sec

    items = ["cs50", "web50", "mobile50", "game50", "test50"]
    return jsonify({"success": True, "items": items})


if __name__ == "__main__":
    app.run()
    
