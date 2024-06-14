from flask import Blueprint, render_template, redirect, url_for, request
from . import db
from .models import User

auth = Blueprint("auth",__name__)

@auth.route("/login")
def login():
    email = request.form.get("email")
    password = request.form.get("password")
    
    return render_template("login.html")

@auth.route("/signup", methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        username = request.form.get("username")
        email = request.form.get("email")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")
        
        email_exists = User.query.filter_by(email=email).first()
    
    print(username)
    print(email)
    print(password1)
    print(password2)
    
    return render_template("signup.html")

@auth.route("/logout", methods=['GET','POST'])
def logout():
    return redirect(url_for("views.home"))


