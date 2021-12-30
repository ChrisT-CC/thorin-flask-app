import os
# import the Flask class
from flask import Flask


# Create an instance of Flask class
app = Flask(__name__)


# use the route decorator to tell Flask what URL should trigger the function that follows
@app.route("/")
def index():
    return "Hello, World"


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)
