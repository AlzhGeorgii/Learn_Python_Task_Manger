from webapp import create_app, db
from webapp.user.models import User
from webapp.project.models import Project, Project_member


app = create_app()

with app.app_context():
    db.create_all()
