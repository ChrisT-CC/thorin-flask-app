import os
import json

# import the Flask class
# Request library is going to handle things like finding out what method was,
# used, and it contains the form object when it's posted
# Flash function in Flask displays a non-permanent message to the user,
# something that only stays on screen until the page is refreshed
# Flask cryptographically signs all of the messages for security purposes,
# so I need to create a secret key
from flask import Flask, render_template, request, flash

# Import env library only if the system can find an env.py file
if os.path.exists("env.py"):
    import env


# Create an instance of Flask class
app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")


# use the route decorator to tell Flask what URL should trigger the function
@app.route("/")
def index():
    return render_template("index.html")


# link about page by routing
@app.route("/about")
def about():
    data = []
    # open the JSON file in order to read it
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("about.html", page_title="About", company=data)


# link about page, member by routing
@app.route("/about/<member_name>")
# create member_name view
def about_member(member_name):
    member = {}
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
        for obj in data:
            if obj["url"] == member_name:
                member = obj
    return render_template("member.html", member=member)


# link contact page by routing
@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        flash("Thanks {}, we received your message!".format(
            request.form.get("name")))
    return render_template("contact.html", page_title="Contact")


# link careers page by routing
@app.route("/careers")
def careers():
    return render_template("careers.html", page_title="Careers")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)
