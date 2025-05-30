from flask import Flask
import os
import datetime

app = Flask(__name__)

@app.route("/")
def hello():
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"""
    <p>ENV = {os.getenv('FLASK_ENV')}</p>
    <p>Updated at: {now}</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
