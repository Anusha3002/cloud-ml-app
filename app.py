import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    cloud = os.environ.get("CLOUD_NAME", "a cloud PaaS")
    return f"<h1>Hello from {cloud} - Anusha (HW1)</h1>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
