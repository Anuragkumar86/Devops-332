from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Multi-stage Build App v2.0</h1>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
