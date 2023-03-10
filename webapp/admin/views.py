from flask import Blueprint, render_template

from webapp.user.decorators import admin_required


blueprint = Blueprint("admin", __name__, url_prefix="/admin")


@blueprint.route("index")
@admin_required
def admin_index() -> str:
    page_title = "Панель администратора"
    return render_template("admin/index.html", page_title=page_title)
