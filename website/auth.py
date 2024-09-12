from flask import Blueprint

auth = Blueprint("auth", __name__)

# call each function whenever the respective path is accessed
@auth.route("/login")
def login():
    return "<p>Login</p>"

@auth.route("/logout")
def logout():
    return "<p>Logout</p>"

@auth.route("/signup")
def signup():
    return "<p>Sign Up</p>"