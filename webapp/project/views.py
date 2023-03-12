from flask import Blueprint, flash, render_template, redirect, url_for
from flask_login import current_user

from webapp import db
from webapp.project.forms import NewProjectForm
from webapp.project.models import Project, Project_member


blueprint = Blueprint("project", __name__, url_prefix="/project")


@blueprint.route("/new")
def project_creation():
    if not current_user.is_authenticated:
        return redirect(url_for("index"))
    page_title = "Новый проект"
    form = NewProjectForm()
    return render_template("project/new.html", page_title=page_title, form=form)


@blueprint.route("/process-new", methods=["POST"])
def process_project_creation():
    form = NewProjectForm()

    if form.validate_on_submit():

        new_project = Project(
            name=form.name.data,
            description=form.description.data,
            date_end=form.date_end.data
        )
        db.session.add(new_project)
        db.session.commit()

        project_owner = Project_member(
            user_id=current_user.id,
            project_id=new_project.id,
            role="owner"
        )
        db.session.add(project_owner)
        db.session.commit()

        flash(f"Проект {new_project.name} создан")
        return redirect(url_for("index"))

    flash("Заполните все поля")
    return redirect(url_for("all_projects"))


@blueprint.route("/all")
def all_projects():
    if not current_user.is_authenticated:
        return redirect(url_for("index"))

    all_projects = Project_member.query.filter(Project_member.user_id == current_user.id).all()

    page_title = "Мои проекты"
    return render_template("project/all.html", page_title=page_title, all_projects=all_projects)
