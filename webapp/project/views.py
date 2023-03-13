from flask import Blueprint, flash, render_template, redirect, url_for
from flask_login import current_user
from flask_login.utils import login_required

from webapp import db
from webapp.project.forms import NewProjectForm
from webapp.project.models import Project, ProjectMember


blueprint = Blueprint("project", __name__, url_prefix="/project")


@blueprint.route("/new")
@login_required
def project_creation():
    form = NewProjectForm()
    return render_template("project/new.html", page_title="Новый проект", form=form)


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

        project_owner = ProjectMember(
            user_id=current_user.id,
            project_id=new_project.id,
            role="owner"
        )
        db.session.add(project_owner)
        db.session.commit()

        flash(f"Проект {new_project.name} создан")
        return redirect(url_for("project.all_projects"))

    flash("Заполните все поля")
    return redirect(url_for("project.project_creation"))


@blueprint.route("/all")
@login_required
def all_projects():
    all_projects = ProjectMember.query.filter(ProjectMember.user_id == current_user.id).all()

    return render_template("project/all.html", page_title="Мои проекты", all_projects=all_projects)
