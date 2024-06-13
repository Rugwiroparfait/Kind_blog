from flask import Blueprint, render_template

auth = Blueprint("auth",__name__)

@auth.route("/login")
def login():
    return("Login")

@auth.route("/sign_up")
def sign_up():
    return("sign up")

@auth.route("logout")
def logout():
    return("Logout")