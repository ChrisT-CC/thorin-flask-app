import os
# import the Flask class
from flask import Flask, render_template


# Create an instance of Flask class
app = Flask(__name__)


# use the route decorator to tell Flask what URL should trigger the function
@app.route("/")
def index():
    return render_template("index.html")


# link about page by routing
@app.route("/about")
def about():
    return render_template("about.html")


# link contact page by routing
@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)
