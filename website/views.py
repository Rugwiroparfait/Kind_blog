from flask import Blueprint, render_template

views = Blueprint("views",__name__)


@views.route("/")
@views.route("/home")
def home():
    return render_template("home.html", name= "Joe", age = 10, id = 12004398 , tel = 783437181, email = "rugwiroparfait003@gmail.com")
