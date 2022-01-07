import os
import json

# import the Flask class
# Request library is going to handle things like finding out what method was
# used, and it contains the form object when it's posted
from flask import Flask, render_template, request


# Create an instance of Flask class
app = Flask(__name__)


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
        print("Hello! Is anybody there?")
        print(request.form.get("name"))
        print(request.form["email"])
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
