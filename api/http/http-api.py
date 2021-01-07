from flask import Flask

app = Flask(__name__)

@app.route("/")
def check_status():
    return "ok"

if __name__ == "__main__":
    app.run()