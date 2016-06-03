from flask import Flask

app = Flask(__name__)


# Create our index or root / route
@app.route("/")
@app.route("/index")
def index():
    return "Python - Hello World! v1.1 - Hi Candace"


if __name__ == "__main__":
    app.run()  # debug="True")
