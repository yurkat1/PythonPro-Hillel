from flask import Blueprint, render_template, redirect, url_for,  flash, session
from werkzeug.security import generate_password_hash
from extensions import db
from models import User
from forms import RegistrationForm, LoginForm
from auth import login_required, authenticate

app = Blueprint("app", __name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        username = form.username
        password = form.password
        hashed_password = generate_password_hash(password.data)
        user = User(username=username.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash("Registration successful! Log in now!", "success")
        return redirect(url_for("app.login"))
    return render_template("register.html", form=form)

@app.route("/login", methods = ["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = authenticate(form.username.data, form.password.data)
        if user:
            session["user_id"] = user.id
            session["username"] = user.username
            flash("Login successfull!", "success")
            return redirect(url_for("app.my_page"))
        return flash("Invalid credentials", "danger")
    return render_template("login.html", form=form)

@app.route("/dashboard")
def dashboard():
    user_count = User.query.count()
    return render_template("dashboard.html", user_count=user_count)

@app.route("/logout")
def logout():
    session.pop("user_id", None)
    session.pop("username", None)
    flash("Logged out", "info")
    return redirect(url_for("app.home"))

@app.route("/my_page")
@login_required
def my_page():
    if "user_id" not in session:
        flash("Please log in first!", "warning")
        return redirect(url_for("app.login"))
    username = session.get("username")
    return render_template("my_page.html", username=username)













