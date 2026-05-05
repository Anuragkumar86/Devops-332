from flask import Flask
import os

app = Flask(__name__)

APP_VERSION = os.getenv("APP_VERSION", "1.0")
PORT        = int(os.getenv("PORT", 5000))

@app.route("/")
def home():
    return f"<h1>Hello from Docker!</h1><p>App Version: {APP_VERSION}</p>"

@app.route("/health")
def health():
    return {"status": "healthy", "version": APP_VERSION}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT, debug=False)
