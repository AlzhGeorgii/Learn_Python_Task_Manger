from flask import Blueprint, flash, render_template, redirect, url_for
from flask_login import current_user, login_user, logout_user

from webapp import db
from webapp.user.forms import LoginForm, RegistrationForm
from webapp.user.models import User


blueprint = Blueprint("user", __name__, url_prefix="/user")


@blueprint.route("/login")
def login():
    if current_user.is_authenticated:
        return redirect(url_for("index"))
    page_title = "Авторизация"
    form = LoginForm()
    return render_template("user/login.html", page_title=page_title, form=form)


@blueprint.route("/process-login", methods=["POST"])
def process_login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter(User.username == form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            flash("Вы успешно вошли на сайт")
            return redirect(url_for("project.all_projects"))

    flash("Неправильные имя или пароль")
    return redirect(url_for("user.login"))


@blueprint.route("/logout")
def logout():
    logout_user()
    flash("Вы успешно разлогинились")
    return redirect(url_for("index"))


@blueprint.route("/registration")
def registration():
    if current_user.is_authenticated:
        return redirect(url_for("index"))
    page_title = "Регистрация"
    form = RegistrationForm()
    return render_template("user/registration.html", page_title=page_title, form=form)


@blueprint.route("/process-registration", methods=["POST"])
def process_registration():
    form = RegistrationForm()

    if form.validate_on_submit():
        new_user = User(username=form.username.data, email=form.email.data, role="user")
        new_user.set_password(form.password.data)
        db.session.add(new_user)
        db.session.commit()
        flash("Вы успешно зарегестрировались")
        return redirect(url_for("user.login"))
    else:
        for field, errors in form.errors.items():
            for error in errors:
                flash(f"Ошибка в поле {getattr(form, field).label.text}: {error}")
        return redirect(url_for("user.registration"))
